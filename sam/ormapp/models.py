from django.db import models
from django.contrib import admin


class car_DB(models.Model):
	customer_name=models.CharField(max_length=15)
	car_model_no=models.IntegerField()
	cost_of_car=models.IntegerField()
	manufacture_date=models.DateField()
	VIN_number=models.IntegerField(primary_key=True)
	
class car_DBAdmin(admin.ModelAdmin):
	list_display=["customer_name","car_model_no","cost_of_car","manufacture_date","VIN_number"]

# Create your models here.
