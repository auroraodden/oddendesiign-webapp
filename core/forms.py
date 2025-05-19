from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            "product",
            "group_name",
            "concept_description",
            "uploaded_file",
            "full_name",
            "email",
            "phone",
            "address",
            "postal_code",
            "city",
            "birth_date",
            "color_1",
            "color_2",
            "color_3",
            "color_4",
            "color_5",
            "agree_to_terms",
            "total_price"
        ]

        labels ={
            "product": "Vennligst velg produkt",
            "group_name": "Russenavn",
            "concept_description": "Beskriv ditt konsept",
            "uploaded_file": "Last opp fil (valgfritt)",
            "full_name": "Fullt navn",
            "email": "E-post",
            "phone": "Telefonnummer",
            "address": "Adresse",
            "postal_code": "Postnummer",
            "city": "By",
            "birth_date": "Fødselsdato",
            "color_1": "Farge 1",
            "color_2": "Farge 2",
            "color_3": "Farge 3",
            "color_4": "Farge 4",
            "color_5": "Farge 5",
            "agree_to_terms": "Jeg godkjenner betingelsene og vilkårene",
            "total_price": "Total sum (NOK)",
        }

        widgets = {
            "birth_date": forms.DateInput(attrs={"type": "date"}),
            "color_1": forms.TextInput(attrs={"type": "color"}),
            "color_2": forms.TextInput(attrs={"type": "color"}),
            "color_3": forms.TextInput(attrs={"type": "color"}),
            "color_4": forms.TextInput(attrs={"type": "color"}),
            "color_5": forms.TextInput(attrs={"type": "color"}),
            "agree_to_terms": forms.CheckboxInput(),
            "total_price": forms.NumberInput(attrs={"readonly": "readonly"}),
        }

    def clean_agree_to_terms(self):
        agreed = self.cleaned_data.get('agree_to_terms')
        if not agreed:
            raise forms.ValidationError("Du må godkjenne betingelsene for å kunne bestille.")
        return agreed
