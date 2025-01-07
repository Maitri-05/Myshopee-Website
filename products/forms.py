from django import forms

class CategoryForm(forms.Form):
    category_name = forms.CharField(label="Enter category name :", max_length=100,required=False,widget=forms.TextInput(attrs={'id':'category_name'}))
    category_thumbnail = forms.FileField(label="Enter Category Image :",widget=forms.FileInput(attrs={'id':'category_thumbnail'}))
    
