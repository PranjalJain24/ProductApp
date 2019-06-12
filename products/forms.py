from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    
    title= forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder":"Your Title"}))
    email= forms.EmailField()
    description= forms.CharField(
                        required=False,
                        widget=forms.Textarea(
                            attrs={
                                "plaeholder" : "Your description",                            
                                "class" : "new_class_name two",
                                "id":"my-id-for-txtarea ",
                                "rows":10,
                                "column":20
                            }
                        )
                    )
    price = forms.DecimalField(initial=999.99 )
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]
    def clean_title(self,*args,**kwargs):
        title=self.cleaned_data.get('title')
        if not "Abc" in title:
            raise forms.ValidationError("This is not a valid title")
        if not "xyz" in title:
            raise forms.ValidationError("This is not a valid title")
        return title
    
    def clean_email(self,*args,**kwargs):
        email=self.cleaned_data.get("email")
        if not email.endswith("edu"):
            raise forms.ValidationError("This is not valid mail ID")
    
        
class RawProductForm(forms.Form):
    
    title= forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder":"Your Title"}))
    description = forms.CharField(
                        required=False,
                        widget=forms.Textarea(
                            attrs={
                                "plaeholder" : "Your description",                            
                                "class" : "new_class_name two",
                                "id":"my-id-for-txtarea ",
                                "rows":10,
                                "column":20
                            }
                        )
                    )
    price = forms.DecimalField(initial=999.99 )
    