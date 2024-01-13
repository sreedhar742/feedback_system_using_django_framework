from django import forms



class Sirform(forms.Form):
    name=forms.CharField()
    id_name=forms.IntegerField()
    
class Collegeform(forms.Form):
    st_name=forms.CharField(label="first name",max_length=100)
    ft_name=forms.CharField(max_length=100)
    mt_name=forms.CharField(max_length=100)
    
    

class RegistrationForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Last Name', max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    id_name = forms.CharField(label='ID', max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    gmail = forms.EmailField(label='Gmail', required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Create Password', max_length=100, required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
