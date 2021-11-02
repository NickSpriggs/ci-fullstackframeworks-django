from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    #inherits all the functionality of forms.ModelForm
    class Meta:
        #Meta gives form information about itself such as display
        model = Item
        fields = ['name', 'done']