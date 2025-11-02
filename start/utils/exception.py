from rest_framework.exceptions import APIException
from rest_framework.views import exception_handler
def my_exception(exc, context):
    response = exception_handler(exc, context)
    if response is not None and isinstance(exc, APIException):
        if hasattr(exc, 'status_code') and exc.status_code:
            response.data['status_code'] = exc.status_code
    return response
class EmailNotFoundException(APIException):
    status_code = 404
    default_detail = '未找到指定的电子邮件。'
    default_code = 'email_not_found'
