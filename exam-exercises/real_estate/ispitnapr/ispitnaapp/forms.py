from django import forms

from ispitnaapp.models import RealEstate


class RealEstateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RealEstateForm,self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = RealEstate
        fields = ['name', 'area', 'description', 'image',]