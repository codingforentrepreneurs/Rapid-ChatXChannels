from django import forms


class ComposeForm(forms.Form):
    message = forms.CharField(
            widget=forms.TextInput(
                attrs={"class": "form-control"}
                )
            )