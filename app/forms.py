from django import forms
from .models import Post, Image, Video, PDF

from django import forms

from django import forms


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result


class PostImageForm(forms.Form):
    file_field = MultipleFileField(required=False)


class PostVideoForm(forms.Form):
    file_field = MultipleFileField(required=False)


class PostPDFForm(forms.Form):
    file_field = MultipleFileField(required=False)

# class MultipleFileInput(forms.ClearableFileInput):
#     allow_multiple_selected = True
#
#
# class MultipleFileField(forms.FileField):
#     def __init__(self, *args, **kwargs):
#         kwargs.setdefault("widget", MultipleFileInput())
#         super().__init__(*args, **kwargs)
#
#     def clean(self, data, initial=None):
#         single_file_clean = super().clean
#         if isinstance(data, (list, tuple)):
#             result = [single_file_clean(d, initial) for d in data]
#         else:
#             result = single_file_clean(data, initial)
#         return result
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description']
#
# class PostImageForm(forms.ModelForm):
#     class Meta:
#         model = Image
#         fields = ['image']
#         widgets = {
#             'image':MultipleFileField()
#         }
#
# class PostVideoForm(forms.ModelForm):
#     class Meta:
#         model = Video
#         fields = ['video']
#         widgets = {
#             'video': MultipleFileField()
#
#         }
#
# class PostPDFForm(forms.ModelForm):
#     class Meta:
#         model = PDF
#         fields = ['pdf']
#         widgets = {
#             'pdf': MultipleFileField()
#
#         }

