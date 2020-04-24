from django import forms
from .models import RSS_URLS, Feed

class InputURLS(forms.Form):
    url1 = forms.URLField()
    url2 = forms.URLField(required=False)
    url3 = forms.URLField(required=False)

    def __init__(self, *args, **kwargs):
        super(InputURLS, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

    # def clean(self):
    #     cleaned_data = super(InputURLS, self).clean()
    #     url1 = cleaned_data.get('url1')
    #     url2 = cleaned_data.get('url2')
    #     url3 = cleaned_data.get('url3')
    #     if not url1 or not url2 or not url3:
    #         raise forms.ValidationError('You have to choose or input something!')

# class SelectURLS(forms.ModelForm):
#     class Meta:
#         model = RSS_URLS
#         fields= ('url',)
#
#     def __init__(self, *args, **kwargs):
#         super(SelectURLS, self).__init__(*args, **kwargs)
#         for field in self.fields:
#             self.fields[field].widget.attrs.update({'class': 'form-control'})
