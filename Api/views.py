from django.contrib.auth import authenticate

from .models import *
from .serializers import *

from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .functions import get_user_by_token

#Получение и добавление пользователей
class UsersView(ListCreateAPIView):
    serializer_class = UserSerializer

    def get(self, request):
        users = User.objects.all()
        serializer = self.get_serializer(users, many=True)
        return Response({"Пользователи": serializer.data})

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Создан пользователь": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Авторизация и создание токена
class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(request, email=email, password=password)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Ошибка аутентификации'}, status=status.HTTP_401_UNAUTHORIZED)

#Получение списка билетов и создание нового    
class TiketsView(ListCreateAPIView):
    serializer_class =  TicketSerializer

    #Получение списка
    def get(self, request):
        token = request.GET.get('token', None)
        user = get_user_by_token(token)
        if not user:
            return Response({"error": f"Ошибка авторизации: {token} не найден"})
        tickets = Ticket.objects.all()
        serializer = self.serializer_class(tickets, many=True)
        return Response({"Билеты": serializer.data})
    
    #Создание билета
    def post(self, request):
        token = request.GET.get('token', None)
        user = get_user_by_token(token)
        if not user:
            return Response({"error": "Пользователь не найден"})
        if user.role == Role.objects.get(id=3):
            return Response({"error": "У вас не достаточно прав"})
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({f"Билет создан": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Работа с отдельными билетами   
class TiketView(RetrieveUpdateDestroyAPIView):
    serializer_class =  TicketSerializer
    
    #Получение билета
    def get(self, request):
        token = request.GET.get('token', None)
        user = get_user_by_token(token)
        if not user:
            return Response({"error": "Пользователь не найден"})
        tikcet_id = request.data.get('id', None)
        if not tikcet_id:
            return Response({"error": "Id билета не был получен"})
        try:
            ticket = Ticket.objects.get(id=tikcet_id)
            serializer = self.serializer_class(ticket)
            return Response({"Билет": serializer.data})
        except Ticket.DoesNotExist:
            return Response({"error": "Билет не найден"})
    
    #Обновление билета
    def put(self, request):
        token = request.GET.get('token', None)
        user = get_user_by_token(token)
        if not user:
            return Response({"error": "Пользователь не найден"})
        if user.role == Role.objects.get(id=3):
            return Response({"error": "У вас не достаточно прав"})
        tikcet_id = request.data.get('id', None)
        if not tikcet_id:
            return Response({"error": "Id билета не был получен"})
        try:
            ticket = Ticket.objects.get(id=tikcet_id)
            serializer = self.serializer_class(ticket, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({f"Билет обновлен": serializer.data})
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Ticket.DoesNotExist:
            return Response({"error": "Билет не найден"})

    #Удаление билета   
    def delete(self, request):
        token = request.GET.get('token', None)
        user = get_user_by_token(token)
        if not user:
            return Response({"error": "Пользователь не найден"})
        if user.role == Role.objects.get(id=3):
            return Response({"error": "У вас не достаточно прав"})
        ticket_id = request.data.get('id', None)
        if not ticket_id:
            return Response({"error": "Id билета не был получен"})
        try:
            ticket = Ticket.objects.get(id=ticket_id) 
            ticket.delete()
            return Response({"error": "Билет удален"})
        except Ticket.DoesNotExist:
            return Response({"error": "Билет не найден"})
