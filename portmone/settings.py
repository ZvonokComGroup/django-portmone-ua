from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.utils.functional import lazy


def get_url(name):
    return 'https://{}{}'.format(get_current_site(request=None), reverse(name))


URL = getattr(settings, 'PORTMONE_GATEWAY_URL', 'https://www.portmone.com.ua/gateway/')
PAYEE_ID = getattr(settings, 'PORTMONE_PAYEE_ID')
SHOP_SITE_ID = getattr(settings, 'PORTMONE_SHOP_SITE_ID')
SUCCESS_URL = getattr(settings, 'PORTMONE_SUCCESS_URL',
                      lazy(lambda: get_url('portmone-success'), str),
                      )()
FAILURE_URL = getattr(settings, 'PORTMONE_FAIL_URL',
                      lazy(lambda: get_url('portmone-fail'), str),
                      )()
LOGIN = getattr(settings, 'PORTMONE_LOGIN', '')
CHECK_IP_ENABLED = getattr(settings, 'PORTMONE_CHECK_IP_ENABLED', True)
IP_LIST = getattr(settings, 'PORTMONE_IP_LIST', [])
