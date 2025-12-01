from django import forms
from .models import Recipe, Ingredient, Instruction


class RecipeForm(forms.ModelForm):
    """Form for the Recipe model."""
    cook_time = forms.IntegerField(
        label="Cook time (minutes)",
        widget=forms.NumberInput(attrs={'placeholder': 'e.g., 30'})
    )

    class Meta:
        model = Recipe
        fields = ['name', 'category', 'cost', 'rating']
        widgets = {
            'cost': forms.NumberInput(attrs={'placeholder': 'e.g., 15.50'}),
            'rating': forms.NumberInput(attrs={'placeholder': 'e.g., 4.5', 'min': '0', 'max': '5', 'step': '0.1'}),
        }

IngredientFormSet = forms.inlineformset_factory(
    Recipe,
    Ingredient,
    fields=('quantity', 'unit', 'name'),
    extra=3,
    can_delete=True,
    widgets={
        'name': forms.TextInput(attrs={'placeholder': 'Ingredient Name (e.g. Flour)'}),
        'quantity': forms.NumberInput(attrs={'placeholder': 'Qty'}),
        'unit': forms.TextInput(attrs={'placeholder': 'Unit'}),
    }
)
InstructionFormSet = forms.inlineformset_factory(
    Recipe,
    Instruction,
    fields=('description',),
    extra=3, 
    can_delete=True,
    widgets={'description': forms.Textarea(attrs={'rows': 2})}
)