from django import forms
from django.forms.widgets import HiddenInput
from .models import Player

class PlayerUpdateForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget = HiddenInput()
        self.fields['uuid'].widget = HiddenInput()
        self.fields['imageUrl'].widget = HiddenInput()
        self.fields['event01'].widget.attrs.update({'class':'form-control', 'style': ' background-color: #212121; color: #FFFFFF;'})
        self.fields['event02'].widget.attrs.update({'class':'form-control', 'style': ' background-color: #212121; color: #FFFFFF;'})
        self.fields['event03'].widget.attrs.update({'class':'form-control', 'style': ' background-color: #212121; color: #FFFFFF;'})
        self.fields['event04'].widget.attrs.update({'class':'form-control', 'style': ' background-color: #212121; color: #FFFFFF;'})
        self.fields['event05'].widget.attrs.update({'class':'form-control', 'style': ' background-color: #212121; color: #FFFFFF;'})
        self.fields['event06'].widget.attrs.update({'class':'form-control', 'style': ' background-color: #212121; color: #FFFFFF;'})
        self.fields['event07'].widget.attrs.update({'class':'form-control', 'style': ' background-color: #212121; color: #FFFFFF;'})
        self.fields['event08'].widget.attrs.update({'class':'form-control', 'style': ' background-color: #212121; color: #FFFFFF;'})
        self.fields['event09'].widget.attrs.update({'class':'form-control', 'style': ' background-color: #212121; color: #FFFFFF;'})
        self.fields['event10'].widget.attrs.update({'class':'form-control', 'style': ' background-color: #212121; color: #FFFFFF;'})
        self.fields['event11'].widget.attrs.update({'class':'form-control', 'style': ' background-color: #212121; color: #FFFFFF;'})
        self.fields['event12'].widget.attrs.update({'class':'form-control', 'style': ' background-color: #212121; color: #FFFFFF;'})