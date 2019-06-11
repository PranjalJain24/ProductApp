from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]
        
class RawProductForm(forms.Form):
    title= forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder":"Your Title"}))
    description= forms.CharField(
                        required=False,
                        widget=forms.Textarea(
                            attrs={
                                "plaeholder" : "Your description"                            
                                "class" : "new_class_name two",
                                "id":"my-id-for-txtarea ",
                                "rows":10,
                                "column":20
                            }
                        )
                    )
    price = forms.DecimalField(initial=999.99 )