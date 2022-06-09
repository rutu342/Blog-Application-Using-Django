from logging import PlaceHolder
from django import forms
from .models import Post,Category,Comment
choices =Category.objects.all().values_list('name','name')
choices_list =[]
for item in choices:
    choices_list.append(item)
#choices =[('coding','coding'),('sports','sports'),('entertainment','entertainment')]
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author','category','body','snippet','image')
        widgets ={
            'title': forms.TextInput(attrs={'class':'form-control','PlaceHolder':'Enter your title here'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.TextInput(attrs={'class':'form-control','value':'','id':'elder','type':'hidden'}),
            'category':forms.Select(choices=choices_list,attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
            'snippet':forms.Textarea(attrs={'class':'form-control'}),
        }
class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','body','snippet')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control','PlaceHolder':'Enter title for you Blog'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control'}),
            #'author':forms.Select(attrs={'class':'form-control'}),
            'body' : forms.Textarea(attrs={'class':'form-control'}),
            'snippet':forms.Textarea(attrs={'class':'form-control'}),
        }
class CommentForm(forms.ModelForm):
    class Meta:
        model= Comment
        fields= ('name','body')
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
        }
