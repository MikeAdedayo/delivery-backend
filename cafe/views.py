from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Users,Cafete,Orders,Orderlist
from .serializers import UsersSerializer,CafeteSerilizer,OrderListSerializer

class UserList(APIView):

    def get(self, request):
        user=Users.objects.all()
        serializer = UsersSerializer(user,many=True)
        return Response(serializer.data)

     # def post(self):

class AuthUser(APIView):

    def get(self,request,username):
        user=get_object_or_404(Users, username=username)
        serializer = UsersSerializer(user)
        return Response(serializer.data)

class CreateUser(generics.CreateAPIView):
    serializer_class= UsersSerializer

class Foodlist(APIView):

    def get(self, request):
        food = Cafete.objects.all()

        serializer= CafeteSerilizer(food,many=True)
        return Response(serializer.data)

class Order(APIView):
        def get(self,request):
            orl=Orderlist.objects.all()
            serializer = OrderListSerializer(orl, many=True)
            return Response(serializer.data)

        def post(self,request):
            data = request.data





            order=Orders.objects.create(order_by=get_object_or_404(Users, username="tola"))
            for i in data:

                orderlist = Orderlist(
                order_id=order,
                food_name=i['food_name'],
                food_quantity=i['food_quantity'],
                quantity_price=i['quantity_price'],
                )
                orderlist.save()


