from datetime import datetime, timedelta

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from datetime import date
from django.template import loader
from django.shortcuts import redirect
from django.views import generic
from django.utils import timezone
from django.core.mail import send_mail, send_mass_mail
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.views import redirect_to_login

from .models import Device, Manufacturer, DeviceDocUpload, CustomerDetails
from .forms import DeviceForm, DeivceDocUploadForm, ManuForm, CustomerDetailsForm, DeviceModelForm


# Create your views here.
def device_actions(request):
    print(">>>>>>>>>>>>: ", request.method)
    # CRUD operations - create, read, update, delete

    # Create a device
    d = Device(
        device_name='AirtelHDNewDevice',
        device_type='Broadcast',
        device_maker=Manufacturer.objects.get(pk=1),
        device_make_date=date.today()
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


# login enter username password -> views -> authenciated ->
# save to cookie login information -> profile page -> close window
# profile page -> get cookie -> un & pwd -> use -> profile page -> cookie expired ->
# cookie deleted -> redirect login page

# Cookies set and get
# def set_dev_cookie(request):
#     resp = HttpResponse("Set Cookie Page")
#     resp.set_cookie("cust_email", "cust_email@email.com")
#     resp.set_cookie("pass", "aasdf")
#     return resp


def set_dev_cookie(request):
    base_html = "<h1>Welcome to Device Portal</h1>"
    resp = HttpResponse(base_html)
    if request.COOKIES.get('visits'):
        visit_count = int(request.COOKIES.get('visits'))
        resp.set_cookie('visits', visit_count + 1)#, max_age=None, expires=datetime.today() + timedelta(seconds=60))
    else:
        visit_count = 1
        resp.set_cookie('visits', visit_count)#, max_age=None, expires=datetime.today() + timedelta(seconds=60))

    return resp


def get_dev_cookie(request):
    if 'visits' in request.COOKIES:
        cke = request.COOKIES['visits']
    else:
        return HttpResponse("Cookie was not saved or it is removed.")
    return HttpResponse(f"Cookie: {cke}")

def cookie_demo(request):
    if request.COOKIES.get('visits') is not None:
        value = request.COOKIES.get('visits')
        html = "<center><h1>You have requested this page {} times</h1></center>".format(value)
        resp = HttpResponse(html)
        resp.set_cookie('visits', int(value) + 1)
        return resp
    else:
        return redirect('/deviceapp/set_dev_cookie/')


# Test browser capability to store cookies
def test_cookie_session(request):
    request.session.set_test_cookie()
    return HttpResponse("<h1>Set Test Cookie</h1>")

def test_cookie_delete(request):
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        response = HttpResponse("Set Test Cookie<br> This is the newly created cookie")
    else:
        response = HttpResponse("Set Test Cookie <br> Sorry!! your browser does not accept cookies")
    return response


# Session apis
def create_session(request):
    request.session['cust_name'] = 'Rajendra'
    request.session['cust_email'] = 'rajendra@email.com'
    # Set expiry
    request.session.set_expiry(0)

    return HttpResponse("<h1>Welcome to Device Portal<br> The Session is Set!</h1>")


def get_session(request):
    cust_name = request.session.get('cust_name')
    cust_email = request.session.get('cust_email')
    context = {'cust_name': cust_name, 'cust_email': cust_email}
    return render(request, "./session_templates/session_info.html", context)


def delete_session(request):
    try:
        # del request.session["cust_name"]
        # del request.session["cust_email"]
        # To remove expired sessions from DB
        request.session.flush()
        request.session.clear_expired()
    except KeyError:
        pass

    return HttpResponse("Session Data cleared")


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


class UserAccessMixin(PermissionRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect_to_login(
                self.request.get_full_path(),
                'user_login',
                self.get_redirect_field_name()
            )

        # guest page, display message
        if not self.has_permission():
            return redirect('user_login')

        return super(UserAccessMixin, self).dispatch(request, *args, **kwargs)


class ManuUpdateView(UserAccessMixin, generic.UpdateView):
    # specify the model you want to use
    model = Manufacturer
    permission_required = 'fake_permission'
    # permission_required = 'deviceapp.change_manufacturer'
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
def device_model_form_func_view(request):
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request (binding):
        dev = DeviceModelForm(request.POST)
        # Check if the form is valid:
        if dev.is_valid():
            print("Device name: ", dev.cleaned_data['device_name'])
            print("Device desc: ", dev.cleaned_data['description'])
            return HttpResponse("Successfully submitted.")
        # else:
        #     return HttpResponseBadRequest("Invalid data")

    # If this is a GET (or any other method) create the default form.
    else:
        dev = DeviceModelForm()
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
    return render(request, "manufacturer_form.html", {'form': dev})


# Form processing
def show_device_doc(request):
    all_data = DeviceDocUpload.objects.all()
    context = {
        'data': all_data
    }
    return render(request, 'device_files.html', context)


def upload_doc(request):
    if request.method == 'POST':
        form = DeivceDocUploadForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['doc_name']
            the_files = form.cleaned_data['doc_data']
            DeviceDocUpload(doc_name_lbl=name, doc_name=the_files).save()
            return HttpResponse("Device document is successfully uploaded.")
        else:
            return HttpResponse('error')
    else:
        context = {
            'form': DeivceDocUploadForm()
        }
        return render(request, 'device_upload_form.html', context)


# View to upload and save customer details
# this view will also send mail to the customer email
def customer_details_upload(request):
    if request.method == 'POST':
        form = CustomerDetailsForm(request.POST, request.FILES)
        print("form.isvalid: ", form.is_valid())
        if form.is_valid():
            fname = form.cleaned_data['fname']
            lname = form.cleaned_data['lname']
            contact = form.cleaned_data['contact']
            photo = form.cleaned_data['photo']
            email = form.cleaned_data['email']
            cd = CustomerDetails(
                fname=fname,
                lname=lname,
                contact=contact,
                photo=photo,
                email=email,
            )
            cd.save()   # Save to the database

            # Here send out an email to customer on successful registration
            # send_mail(
            #     'Welcome to Sandisk user group!',
            #     'We are happy to have you as our customer. Please write to us in case of any queries.',
            #     'rajenrishi@hotmail.com',
            #     [email],
            # )
            message1 = (
                'Message1',
                'Mass email message1',
                'rajenrishi@hotmail.com',
                ['rajenrishi@gmail.com']
            )
            message2 = (
                'Message2',
                'Mass email message2',
                'rajenrishi@hotmail.com',
                ['jesuabhishek@gmail.com']
            )
            send_mass_mail((message1, message2), fail_silently=False)

            return HttpResponse("Customer is successfully added.")
        else:
            return HttpResponse('Unable to add the customer.')
    else:
        context = {
            'form': CustomerDetailsForm()
        }
        return render(request, 'customer_upload_form.html', context)

