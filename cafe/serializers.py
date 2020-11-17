from rest_framework import serializers
from django.shortcuts import get_object_or_404
from .models import Users,Cafete,Orders,Orderlist


class UsersSerializer(serializers.ModelSerializer):

 class Meta:
         model = Users
         fields='__all__'

def create(self, validated_data):
        user = Users(
            email = validated_data['username'],
            usermobile =validated_data['usermobile'],
            useremail =validated_data['useremail'],
            userpassword= validated_data['userpassword'],

        )
        user.save()
        return user

class CafeteSerilizer(serializers.ModelSerializer):

    class Meta:
        model = Cafete
        fields= '__all__'

class OrderListSerializer(serializers.ModelSerializer):

    class Meta:
        model= Orderlist
        fields='__all__'



def create(self, validated_data):

        orderlist = Orderlist(
            order_id=Orders.objects.create(order_by=validated_data['username']),
            food_name ="dundu",
            food_quantity = validated_data['food_quantity'],
            quantity_price = validated_data['quantity_price'],
        )
        orderlist.save()

        return Orderlist