from django.forms import ModelForm
from .models import Anotacao


class AnotacaoForm(ModelForm):
    class Meta:
        model = Anotacao
        fields = '__all__'