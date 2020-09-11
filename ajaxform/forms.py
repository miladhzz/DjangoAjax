from django import forms
import datetime
from . import models


class TestForm(forms.Form):
    name = forms.CharField(max_length=100)
    family = forms.CharField(max_length=100)

    def __init__(self, *args, **kwargs):
        super(TestForm, self).__init__(*args, **kwargs)
        # add a "form-control" class to each form input
        # for enabling bootstrap
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })


class FriendForm(forms.ModelForm):
    # change the widget of the date field.
    dob = forms.DateField(
        label='What is your birth date?',
        # change the range of the years from 1980 to currentYear - 5
        widget=forms.SelectDateWidget(years=range(1980, datetime.date.today().year-5))
    )

    def __init__(self, *args, **kwargs):
        super(FriendForm, self).__init__(*args, **kwargs)
        # add a "form-control" class to each form input
        # for enabling bootstrap
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })

    class Meta:
        model = models.Friend
        fields = '__all__'
