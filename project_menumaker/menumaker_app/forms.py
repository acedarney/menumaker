from django import forms
from .models import Recipe, Menu

class MenuForm(forms.ModelForm):
    # menu_name = forms.CharField(label='Current Menu', max_length=50, disabled=True)
    # recipe_name = forms.CharField(label='Recipe Name', max_length=50)
    class Meta:
        model = Menu
        fields = ['name', 'recipes']
