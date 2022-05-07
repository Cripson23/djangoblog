from .models import Posts
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, FileInput, DateTimeField
import datetime


class PostsForm(ModelForm):
    date = DateTimeField(input_formats=['%Y-%m-%d %H:%M:%S'], initial=format(datetime.datetime.now(), '%Y-%m-%dT%H:%M'),
                         widget=DateTimeInput(attrs={
                             'class': 'form-control',
                             'type': 'datetime-local',
                             'placeholder': 'Дата и время публикации',
                         }),
                         localize=True)

    class Meta:
        model = Posts
        fields = "__all__"

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название поста',
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс поста',
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст поста',
            }),
            "image": FileInput(attrs={
                'class': 'form-control',
                'name': 'image',
                'accept': 'image/*',
                'placeholder': 'Изображение поста',
            })
        }
