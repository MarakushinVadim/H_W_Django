from django.core.exceptions import ValidationError
from django.forms import ModelForm, BooleanField

from catalog.models import Product, Version


class StyleFormMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        exclude = ("updated_at", 'created_at',)

    def clean_name(self):
        name = self.cleaned_data['name']
        block_word = ('казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар',)
        for word in block_word:
            if word in name.lower():
                raise ValidationError(f'В имени присутствует запрещенное слово, придумайте другое имя '
                                      f'список запрещенных слов:'
                                      f' {block_word}')
        return name

    def clean_description(self):
        description = self.cleaned_data['description']
        block_word = ('казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар',)
        for word in block_word:
            if word in description.lower():
                raise ValidationError(f'В описании присутствует запрещенное слово, придумайте другое описание '
                                      f'список запрещенных слов:'
                                      f' {block_word}')
        return description


class VersionForm(StyleFormMixin, ModelForm):

    class Meta:
        model = Version
        fields = '__all__'



