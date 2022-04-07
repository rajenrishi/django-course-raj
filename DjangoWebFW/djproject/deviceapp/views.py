from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from datetime import date
from django.template import loader
from django.shortcuts import redirect
from django.views import generic
from django.utils import timezone

from .models import Device, Manufacturer
from .forms import DeviceForm, ManuForm

# Create your views here.
def device_actions(request):
    print(">>>>>>>>>>>>: ", request.method)
    # CRUD operations - create, read, update, delete

    # Create a device
    d = Device(
        device_name='Sandisk8GB',
        device_type='Storage',
        device_maker=Manufacturer.objects.get(pk=1),
        device_make_date=date(2022, 3, 12)
    )
    d.full_clean()
    d.save()

    # Updating fields
    # d = Device.objects.get(device_name='Sandisk32GB')
    # d.device_name = "Sandisk1TB"
    # d.save()

    # latest_post = Device.objects.earliest()
    # print(">>>>>>>>>>>>>>>>>>> ", latest_post)
    #
    # Retrieving objects
    # dor = Device.objects.all()
    # # print(dor)
    # for dev in dor:
    #     print(dev.device_name)

    # df = Device.objects.filter(device_make_year__gt='2001')
    # for dev in df:
    #     print(dev.device_name)
    #
    # df = Device.objects.filter(device_name__startswith='San')
    # for dev in df:
    #     print(dev.device_name)

    # Delete object
    # d = Device.objects.get(device_name='Sandisk128GB')
    # ret = d.delete()
    # print(ret)

    text = """<h1>In django deviceapp page</h1>"""
    return HttpResponse(text)


def show_devices_names(request):
    # Retrieving objects
    dev_list = Device.objects.all()
    print(dev_list)

    template = loader.get_template('disp_device_names.html')
    data = {
        'devices_list': dev_list
    }
    return HttpResponse(template.render(data))

def show_device_info(request, id):
    # Retrieving objects
    try:
        dev = Device.objects.get(pk=id)
        print(dev)
        template = loader.get_template('disp_device_info.html')
        data = {
            'device': dev
        }
        return HttpResponse(template.render(data))
    except:
        return redirect("device_actions", permanent=True)


# Passing model instance in redirect
# def show_first_device(request):
#     dev = Device.objects.all().first()
#     return redirect(dev)


# View name and parameters
# def show_first_device(request):
#     d_id = 8
#     return redirect("show_device_info", id=d_id)

#  URL
def show_first_device(request):
    d_id = 8
    return redirect(f"/deviceapp/show_device_info/{d_id}/")




class DeviceDetailView(generic.DetailView):
    model = Device
    template_name = "disp_device_info.html"
    context_object_name = 'device'
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     print(">>>>>>>>>>>> context: ", context)
    #     context['now'] = timezone.now()
    #     print(">>>>>>>>>>>> context: ", context)
    #     return context


class DeviceListView(generic.ListView):
    model = Device
    template_name = "disp_device_names.html"
    context_object_name = 'devices_list'

    def get_queryset(self):
        return Device.objects.filter(device_maker=1)


class DeviceFormView(generic.FormView):
    # specify the Form you want to use
    form_class = DeviceForm
    # specify name of template
    template_name = "device_form.html"
    # can specify success url
    # url to redirect after successfully
    # updating details
    success_url = "/deviceapp/device_actions"

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.

        # perform a action here
        print(form.cleaned_data)
        return super().form_valid(form)


class ManufacturerCreateView(generic.CreateView):
    # specify the model for create view
    model = Manufacturer
    template_name = "manufacturer_form.html"

    # specify the fields to be displayed
    fields = ['manu_name', 'manu_address']
    success_url = "/deviceapp/device_actions"


class ManuUpdateView(generic.UpdateView):
    # specify the model you want to use
    model = Manufacturer
    template_name = "manufacturer_form.html"

    # specify the fields
    fields = ['manu_name', 'manu_address']

    # can specify success url
    # url to redirect after successfully
    # updating details
    success_url = "/deviceapp/device_actions"


class ManuDeleteView(generic.DeleteView):
    # specify the model you want to use
    model = Manufacturer
    template_name = "manu_delete_confirm.html"

    # can specify success url
    # url to redirect after successfully
    # deleting object
    success_url = "/deviceapp/device_actions"


class DeviceArchiveIndexView(generic.ArchiveIndexView):
    queryset = Device.objects.all()
    date_field = "device_make_date"
    allow_future = True
    template_name = "device_archive.html"
    #
    # def get_queryset(self):
    #     return Device.objects.all()


class DeviceYearArchiveView(generic.YearArchiveView):
    queryset = Device.objects.all()
    date_field = "device_make_date"
    make_object_list = True
    allow_future = True
    template_name = "device_archive_year.html"


class DeviceMonthArchiveView(generic.MonthArchiveView):
    queryset = Device.objects.all()
    date_field = "device_make_date"
    make_object_list = True
    allow_future = True
    template_name = "device_archive_month.html"


class DeviceWeekArchiveView(generic.WeekArchiveView):
    queryset = Device.objects.all()
    date_field = "device_make_date"
    week_format = "%W"
    allow_future = True
    template_name = "device_archive_week.html"


class DeviceDayArchiveView(generic.DayArchiveView):
    queryset = Device.objects.all()
    date_field = "device_make_date"
    allow_future = True
    template_name = "device_archive_day.html"


# Form processing
def device_form_func_view(request):
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request (binding):
        dev = DeviceForm(request.POST)
        # Check if the form is valid:
        if dev.is_valid():
            print("Device name: ", dev.cleaned_data['device_name'])
            print("Device desc: ", dev.cleaned_data['description'])
            return HttpResponse("Successfully submitted.")
        # else:
        #     return HttpResponseBadRequest("Invalid data")

    # If this is a GET (or any other method) create the default form.
    else:
        dev = DeviceForm()
    return render(request, "device_form.html", {'form': dev})















# Form processing
def manu_form_func_view(request):
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request (binding):
        dev = ManuForm(request.POST)
        # Check if the form is valid:
        if dev.is_valid():
            print("manu_name: ", dev.cleaned_data['manu_name'])
            print("manu_name: ", dev.cleaned_data['manu_address'])
            return HttpResponse("Successfully submitted.")
    # If this is a GET (or any other method) create the default form.
    else:
        dev = ManuForm()
    return render(request, "device_form.html", {'form': dev})
