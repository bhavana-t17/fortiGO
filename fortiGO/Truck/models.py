from django.db import models

# Create your models here.
class UserLog(models.Model):
    userlogid = models.AutoField(primary_key = True)
    email = models.CharField(max_length = 150)
    password = models.CharField(max_length = 150)
    name = models.CharField(max_length = 150)
    pincode = models.IntegerField()

'''class Routes(models.Model):
    routeid = models.AutoField(primary_key = True)
    int_st1 = models.CharField(max_length = 150)
    int_st2 = models.CharField(max_length = 150)
    int_st3 = models.CharField(max_length = 150)
    int_st4 = models.CharField(max_length = 150)
    int_st5 = models.CharField(max_length = 150)

class Booking(models.Model):
    booking_id = models.AutoField(primary_key = True)
    user_id = models.ForeignKey(UserLog,on_delete = models.PROTECT)
    route_id = models.ForeignKey(Routes,on_delete = models.PROTECT)
    truck_id = models.ForeignKey(Trucks,on_delete = models.PROTECT)
    source = models.CharField(max_length = 150)
    destination = models.CharField(max_length = 150)
    load_weight = models.CharField(max_length = 150)
    payment_status = models.CharField(max_length = 150)'''
