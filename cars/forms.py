from django import forms
from cars.models import Car


class CarCreateForm(forms.ModelForm):
    brand = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", 
                   "placeholder": "Марка",
                }
        )
    )

    model_auto = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", 
                   "placeholder": "Модель",
                }
        )
    )

    body = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", 
                   "placeholder": "Кузов",
                }
        )
    )

    color = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", 
                   "placeholder": "Цвет",
                }
        )
    )

    instructions = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", 
                   "placeholder": "Инструкции",
                }
        )
    )
    class Meta:
        model = Car
        fields = [
            "brand",
            "model_auto",
            "body",
            "color",
            "instructions",
        ]