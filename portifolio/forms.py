from django import forms
from .models import Email, Category, Portifolio

class EmailForm(forms.ModelForm):
    
    class Meta:
        model = Email
        fields = "__all__"

class CategoryForm(forms.ModelForm):
    
    class Meta:
        model = Category
        fields = "__all__"

class PortifolioForm(forms.ModelForm):
    
    class Meta:
        model = Portifolio
        fields = "__all__"
