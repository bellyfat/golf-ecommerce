from django import forms


class teeTimeForm(forms.Form):
    firstname = forms.CharField(label='First Name')
    lastname = forms.CharField(label='Last Name')
    date = forms.DateField(label='Date')
    time = forms.TimeField(label='Time')
    golfers = forms.IntegerField(label='Number of Golfers')
    contactNumber =forms.IntegerField(label='Phone Number')
    email=forms.EmailField(label='Email')

