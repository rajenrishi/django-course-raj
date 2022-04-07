from django.db import models


class Manufacturer(models.Model):
    manu_name = models.CharField(max_length=30, unique=True, help_text='Device name')
    manu_address = models.CharField(max_length=20, blank=True)

    class Meta:
        db_table = "manufacturer"


class Device(models.Model):
    device_name = models.CharField(max_length=30, unique=True, help_text='Device name')
    device_type = models.CharField(max_length=20, blank=True)
    device_maker = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, null=True, related_name="devices", related_query_name="device")
    device_make_date = models.DateField(blank=True, null=True)

    def get_absolute_url(self):
        return "/deviceapp/show_device_info/{}/".format(self.id)

    class Meta:
        db_table = "device"


class DigitalMart(models.Model):
    mart_name = models.CharField(max_length=30, unique=True, blank=True)
    mart_location = models.CharField(max_length=50, blank=True)
    mart_cus_email = models.EmailField(max_length=50, blank=True)
    mart_address = models.CharField(max_length=50, null=True, blank=True)
    mart_device = models.ManyToManyField(Device, null=True)

    class Meta:
        db_table = "digitalmart"
