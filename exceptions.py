"""
settings配置REST_FRAMEWORK:
    'EXCEPTION_HANDLER': 'conf.exceptions.custom_exception_handler',
"""
import logging
from rest_framework.views import exception_handler

logger = logging.getLogger('request_data')


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        data = {'errcode': response.status_code}

        errmsg = {}
        for key, value in response.data.items():
            if type(value) == list:
                errmsg[key] = value[0]
            else:
                errmsg[key] = value

        data['errmsg'] = errmsg
        response.data = data

    return response
