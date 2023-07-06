from django import forms


class ConverterForm(forms.Form):
    amount = forms.IntegerField(
        label="Amount",
        initial=1,
        widget=forms.NumberInput(attrs={"class": "form-control"}),
    )
    currencies_choices = [("USD", "USD"), ("EUR", "EUR")]
    from_currency = forms.ChoiceField(
        label="From",
        choices=currencies_choices,
        required=True,
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    to_currency = forms.ChoiceField(
        label="To",
        choices=currencies_choices,
        required=True,
        widget=forms.Select(attrs={"class": "form-control"}),
    )
