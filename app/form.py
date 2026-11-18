from django import forms
from decimal import Decimal
from django.core.validators import MinLengthValidator, MaxLengthValidator

GENRE_CHOICES = [
    ('g1', "Drama"),
    ('g2', "Prose"),
    ('g3', "Poetry")

]
def must_start_with_a(value: str):
    if not value.lower().startswith('a'):
        raise forms.ValidationError("Author name must start with  'a' ")
class BookForm (forms.Form):
    title = forms.CharField(
        label='Book Title',
        validators=[MinLengthValidator(3, "must be 3 or more character")],
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    author = forms.CharField(label='Author', initial='book name', validators=[must_start_with_a])
    price = forms.DecimalField(label='Price', decimal_places=2, initial=Decimal(0.00))
    is_available = forms.BooleanField(label='Is It Available', required=False)
    genre = forms.ChoiceField(choices=GENRE_CHOICES, initial='g2')