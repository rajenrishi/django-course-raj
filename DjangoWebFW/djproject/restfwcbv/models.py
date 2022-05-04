from django.db import models


# Create your models here.
class Employee(models.Model):
    first_name = models.CharField("First Name", max_length=50)
    last_name = models.CharField("Last Name", max_length=50)
    age = models.IntegerField("Age")

    class Meta:
        db_table = "employee"
