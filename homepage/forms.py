from django import forms
from .models import CustomUser, Image, Membership, Events


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['student_id', 'agreed_to_terms']

class ImageForm(forms.ModelForm):
    class Meta:
        model=Image
        fields=("image","caption")


class MembershipForm(forms.ModelForm):
    class Meta:
        model = Membership
        fields = ["memberid","membernohp","musicinstrument"]

class EventForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ('eventsName', 'eventsDesc', 'eventsDate')


#class EventUpdateForm(forms.Form):
    #eventName = forms.CharField(label='Event Name', max_length=100)


