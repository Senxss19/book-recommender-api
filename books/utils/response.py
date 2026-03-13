from rest_framework.response import Response


def success(data=None, message="success", code=0):
    return Response({
        "code": code,
        "message": message,
        "data": data
    })


def error(message="error", code=1, data=None):
    return Response({
        "code": code,
        "message": message,
        "data": data
    })