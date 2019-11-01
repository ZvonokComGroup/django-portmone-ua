import decimal

from portmone import settings


def getBodyRequest(description: str, shopOrderNumber: str, billAmount: decimal.Decimal,
                   billCurrency: str, emailAddress: str, lang: str = 'uk') -> dict:
    return {
        "paymentTypes": {"card": "Y", "portmone": "N", "token": "N", "masterpass": "Y",
                         "visacheckout": "Y", "createtokenonly": "N"},
        "priorityPaymentTypes": {"card": "1", "portmone": "2", "qr": "0", "masterpass": "0",
                                 "token": "0", "visacheckout": "1", "createtokenonly": "0"},
        "payee": {"payeeId": settings.PAYEE_ID,
                  "shopSiteId": settings.SHOP_SITE_ID,
                  "login": settings.LOGIN,
                  "dt": "",
                  "signature": ""},
        "order": {"description": description, "shopOrderNumber": shopOrderNumber,
                  "billAmount": str(billAmount), "attribute1": "1", "attribute2": "2",
                  "attribute3": "3",
                  "attribute4": "4", "attribute5": "", "successUrl": str(settings.SUCCESS_URL),
                  "failureUrl": str(settings.FAILURE_URL),
                  "preauthFlag": "N", "billCurrency": billCurrency, "encoding": ""},
        "token": {"tokenFlag": "N", "returnToken": "N", "token": "", "cardMask": "",
                  "otherPaymentMethods": "Y", "sellerToken": ""},
        "payer": {"lang": lang, "emailAddress": emailAddress},
        "style": {"type": "light", "logo": "", "backgroundColorHeader": "",
                  "backgroundColorButtons": "", "colorTextAndIcons": "",
                  "borderColorList": "", "bcMain": ""}
    }
