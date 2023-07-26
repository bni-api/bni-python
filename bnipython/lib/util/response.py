def responseOGP(params={'res', 'resObj'}):
    try:
        if (params['res'][params['resObj']]['parameters']['responseCode'] != '0001'):
            code = params['res'][params['resObj']]['parameters']['responseCode']
            responseMessage = params['res'][params['resObj']]['parameters']['responseMessage']
            errorMessage = params['res'][params['resObj']]['parameters']['errorMessage']
            raise ValueError(f'errorMessage: {errorMessage}, responseMessage: {responseMessage}, code: {code}')
        else:
            return params['res']
    except Exception:
        code = params['res']['Response']['parameters']['responseCode']
        message = params['res']['Response']['parameters']['responseMessage']
        raise ValueError(f'{code}:{message}')


def responseSnapBI(params={'res'}):
    statusCodeSuccess = [
        '2000000',
        '2001100',
        '2001400',
        '2001500',
        '2001600',
        '2001700',
        '2001800',
        '2002200',
        '2002300',
        '2003600',
        '2007300'
    ]
    if not params['res']['responseCode'] in statusCodeSuccess:
        raise ValueError(
            f"{params['res']['responseCode']} : {params['res']['responseMessage']}")
    return params['res']

def responseRDN(params={'res'}):
    try:
        if (params['res']['response']['responseCode'] != '0001'):
            code = params['res']['response']['responseCode']
            responseMessage = params['res']['response']['responseMessage']
            errorMessage = params['res'][params['resObj']]['response']['errorMessage']
            raise ValueError(f'errorMessage: {errorMessage}, responseMessage: {responseMessage}, code: {code}')
        else:
            return params['res']
    except Exception:
        code = params['res']['response']['responseCode']
        message = params['res']['response']['responseMessage']
        raise ValueError(f'{code}:{message}') 
