from django import forms

multiply_help_text = 'Multiply Number (2 for twice, 0.3 for third)'
file_upload_help_text = "Recipe File (image or a pdf)"

class FileAndNumForm(forms.Form):

    
    number = forms.FloatField(required=True)
    file = forms.FileField(required=True)


    
