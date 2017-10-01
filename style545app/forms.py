from django import forms
from style545app.models import Itemmaster
from style545app.models import Looksmaster
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class Itemselector(forms.Form):
    item_list = Itemmaster.objects.values_list('item_price','item_name').order_by('-item_name')
    greeting=forms.CharField(label='Select atleast 5 looks')
    i=1
    while (i<=5):
     selffield= forms.ChoiceField(item_list, widget=forms.Select(attrs={
                               "onChange":'getprice(this.value,1);'}))
     i=i+1

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')


    class Meta:
        model = User
        fields = ('username', 'email', 'first_name','last_name','password1','password2')
