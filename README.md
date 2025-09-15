# Ex02 Django ORM Web Application
# Date:15/09/2025
# AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

# ENTITY RELATIONSHIP DIAGRAM
## DESIGN STEPS
## STEP 1:
Clone the problem from GitHub

## STEP 2:
Create a new app in Django project

## STEP 3:
Enter the code for admin.py and models.py

## STEP 4:
Execute Django admin and create details for 10 books

# PROGRAM
'''
admin.py 

from django.contrib import admin
from .models import car_DB,car_DBAdmin
admin.site.register(car_DB,car_DBAdmin)

models.py

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


'''

# OUTPUT
![alt text](<Screenshot 2025-09-15 085628.png>)

# RESULT
Thus the program for creating a database using ORM hass been executed successfully
