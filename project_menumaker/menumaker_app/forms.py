from django import forms
from .models import Recipe, Menu


# class MenuForm(forms.ModelForm):
#     class Meta:
#         model = Menu
#         fields = ('recipes', )
#         widgets = {
#             'recipes': ModelSelect2MultipleWidget(
#                 model=Recipe,
#                 search_fields=['name__icontains']
#             )
#         }
