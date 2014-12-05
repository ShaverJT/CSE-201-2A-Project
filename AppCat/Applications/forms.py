from django import forms

from Applications import models

class ReviewForms(forms.ModelForm):
    class Meta:
        model = models.Review
        
        fields = ['review_name','description','rating']
        exclude = ['app']
        
class AppForms(forms.ModelForm):
    class Meta:
        model = models.App
        fields = ['app_name','developers','description','link','pic',]
        exclude = ['pub_date']