from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token


from auth_app.models import User


@api_view(['POST'])
@permission_classes((AllowAny,))
def login(request):
    """
    URL 	:/services/user/login
    Method	:POST
    """
    email = request.data.get("email")
    password = request.data.get("password")

    print(request.data, request.POST)

    try:
        User.objects.get(email=email)
    except ObjectDoesNotExist:
        # TODO: user has not an account
        return JsonResponse({"message": "invalid email"}, status=400, safe=False)

    user = authenticate(email=email, password=password)

    if user:
        token ,e= Token.objects.get_or_create(user=user)

        responseData = {
            "message": "successful response",
            "code": 200,
            "payload": {
                "userId": user.id,
                "token": token.key
            }
        }

        return JsonResponse(responseData, status=200, safe=False)
    else:
        return JsonResponse({"message": "invalid password"}, status=400, safe=False)







