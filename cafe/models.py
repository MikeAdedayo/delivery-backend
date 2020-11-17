from django.db import models

# Create your models here.
class Cafete(models.Model):
    food_name = models.CharField(max_length=50)
    food_price = models.CharField(max_length=50)
    food_type = models.CharField(max_length=50)
    food_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.food_name

class Users(models.Model):
    username = models.CharField(max_length=50)
    usermobile = models.CharField(max_length=50)
    useremail = models.CharField(max_length=50)
    userpassword = models.CharField(max_length=50)
    user_image = models.CharField(max_length=50)

    def __str__(self):
        return self.username

class Orders(models.Model):
    order_by = models.ForeignKey(Users, on_delete=models.CASCADE)
    def __str__(self):
        return 'Order by'+ self.order_by.username


class Orderlist(models.Model):
    order_id = models.ForeignKey(Orders, on_delete=models.CASCADE)

    food_name = models.CharField(max_length=50)
    food_quantity = models.IntegerField()
    quantity_price = models.IntegerField()

    def __str__(self):
        return self.food_name +' by '+ self.order_id.order_by.username
