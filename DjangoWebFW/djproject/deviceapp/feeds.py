from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords

from .models import Device


class LastDevicesAdded(Feed):
    title = "Device"
    link = ""
    descript = "Device description"

    def items(self):
        return Device.objects.all()

    def item_title(self, item):
        return item.device_name

    def item_description(self, item):
        return truncatewords(item.device_type, 30)
