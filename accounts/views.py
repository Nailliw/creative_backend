from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User


class HelloView(APIView):
    def get(self, request):
        return Response({"message": "hello kenzie"})


class LoginView(APIView):
    def post(self, request):
        username = request.data["username"]
        password = request.data["password"]

        user = User.objects.get(username=username, password=password)

        if user is None:
            return Response({"msg": "Dados incorretos"}, status.HTTP_200_OK)

        return Response(status.HTTP_200_OK)


class SignupView(APIView):
    def post(self, request):
        username = request.data["username"]
        password = request.data["password"]

        res = User.objects.all().filter(username=username)

        if res.values("username") == username:
            print("funfou")
            return Response(
                {"msg": res.values()},
                status.HTTP_200_OK,
            )

        User.objects.create(
            username=username,
            password=password,
        )
        return Response(
            {
                "msg": "Login criado com sucesso!",
            },
            status.HTTP_201_CREATED,
        )
