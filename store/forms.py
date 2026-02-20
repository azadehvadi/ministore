from django import forms
from .models import Product

# class ProductForm(forms.ModelForm):
#     code=forms.CharField(label='کد محصول')
#     name=forms.CharField(label='نام محصول')
#     stock=forms.IntegerField(min_value=0,label='موجودی')
#     price=forms.DecimalField(max_digits=10,decimal_places=2,label='قیمت')
#     description=forms.CharField(label='توضیحات محصول')

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=['code','name','stock','price','description','image']
        labels={
            'code':'کد محصول',
            'name': 'نام محصول',
            'stock': 'موجودی',
            'description': 'توضیحات',
            'image': 'تصاویر',
        }
        widgets={
            'description':
                forms.Textarea(attrs={'rows':5}),
        }


