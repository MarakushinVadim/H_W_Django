from django.core.exceptions import ValidationError
from django.forms import ModelForm

from catalog.models import Product


class ProductForm(ModelForm):
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
