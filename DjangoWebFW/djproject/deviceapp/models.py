from django.db import models


class Manufacturer(models.Model):
    manu_name = models.CharField(max_length=30, unique=True, help_text='Device name')
    manu_address = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.manu_name

    class Meta:
        db_table = "manufacturer"


class Device(models.Model):
    device_name = models.CharField(max_length=30, unique=True, help_text='Device name')
    device_type = models.CharField(max_length=20, blank=True)
    device_maker = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, null=True, related_name="devices", related_query_name="device")
    device_make_date = models.DateField(blank=True, null=True)
    device_image = models.ImageField(null=True, blank=True)

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


class DeviceDocUpload(models.Model):
    doc_name_lbl = models.CharField(max_length=255)
    doc_name = models.FileField(upload_to='')

    def __str__(self):
        return self.doc_name_lbl


class CustomerDetails(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='')
    email = models.EmailField(max_length=255, blank=True)

    def __str__(self):
        return self.fname
