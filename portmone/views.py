import decimal
import logging
from xml.etree import ElementTree as ET

from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from portmone import settings
from portmone.forms import ResultForm
from portmone.models import PortmonePayment
from portmone.signals import result_authorized

logger = logging.getLogger('portmone')

NO_VALID_XML_MSG = 'No valid xml data'
OTHER_NO_VALID = 'Validation Error'


def get_ip_address(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')

    return ip


@csrf_exempt
@require_POST
def authorize_result(request):
    '''
    See documentation:
    https://docs.portmone.com.ua/docs/en/PaymentGatewayEng/#83-notification-of-the-online-store-server-about-the-authorization-result
    '''

    ip = get_ip_address(request)
    if settings.CHECK_IP_ENABLED and ip not in settings.IP_LIST:
        raise Http404

    form = ResultForm(request.POST)
    if form.is_valid():
        data_string = form.cleaned_data['data']
        try:
            root = ET.fromstring(data_string.strip())
        except ET.ParseError as exc:
            logger.warning(exc)
            return HttpResponse(NO_VALID_XML_MSG, status=400)
        code_el = root.find('./BILL/PAYEE/CODE')
        if code_el is None:
            logger.warning('PAYEE CODE tag is not defined')
            return HttpResponse(NO_VALID_XML_MSG, status=400)
        if settings.PAYEE_ID != code_el.text.strip():
            logger.warning('PAYEE CODE is incorrect')
            return HttpResponse(OTHER_NO_VALID, status=400)
        bill_number_el = root.find('./BILL/BILL_NUMBER')  # It is equal to the shop_order_number
        if bill_number_el is None:
            logger.warning('BILL NUMBER tag is not defined')
            return HttpResponse(NO_VALID_XML_MSG, status=400)
        shopOrderNumber = bill_number_el.text.strip()
        try:
            payment = PortmonePayment.objects.get(shopOrderNumber=shopOrderNumber)
        except PortmonePayment.DoesNotExist:
            logger.warning(f'PortmonePayment with shopOrderNumber={shopOrderNumber} dnot exist')
            return HttpResponse('OK')
        payed_amount_el = root.find('./BILL/PAYED_AMOUNT')
        if payed_amount_el is None:
            logger.warning('PAYED AMOUNT tag is not defined')
            return HttpResponse(NO_VALID_XML_MSG, status=400)
        try:
            payedAmount = decimal.Decimal(payed_amount_el.text.strip())
        except decimal.InvalidOperation as exc:
            logger.warning('payedAmount is not decimal')
            return HttpResponse(OTHER_NO_VALID, status=400)
        result_authorized.send(
            sender=payment, shopOrderNumber=shopOrderNumber, payedAmount=payedAmount,
        )
        return HttpResponse('OK')

    else:
        return HttpResponse('Form is not valid', status=400)


@csrf_exempt
def success(request):
    return render(request, 'portmone/success.html')


@csrf_exempt
def fail(request):
    return render(request, 'portmone/fail.html')
