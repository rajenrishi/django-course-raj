from django import forms
from .models import Device, Manufacturer

# creating a form
class DeviceForm(forms.Form):
    # specify fields for model
    device_name = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)

    # def clean_device_name(self):
    #     dev_name = self.cleaned_data.get("device_name")
    #     dn = Device.objects.filter(device_name=dev_name)
    #
    #     if not dn:
    #         raise forms.ValidationError("Device does not exist in our db!")
    #     return dev_name


# creating a form
class DeviceModelForm(forms.ModelForm):

    class Meta:
        model = Device
        fields = '__all__'





# creating a from Model
class ManuForm(forms.ModelForm):

    def clean_manu_name(self):
        pass

    class Meta:
        model = Manufacturer
        fields = ['manu_name', 'manu_address']
        # fields = '__all__'    # not recommended, it poses security risks


class DeivceDocUploadForm(forms.Form):
    doc_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    doc_data = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}))




class CustomerDetailsForm(forms.Form):
    fname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    lname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    contact = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    photo = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
