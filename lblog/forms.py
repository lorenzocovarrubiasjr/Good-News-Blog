from django import forms
from .models import BlogPost 
    
class BlogPostModelForm(forms.ModelForm):
    class Meta:
        model = BlogPost 
        fields = ['title', 'image', 'slug', 'content', 'published_date']
        
    def clean_title(self, *args, **kwargs):
        instance = self.instance 
        title = self.cleaned_data.get('title')
        qs = BlogPost.objects.filter(title__iexact=title)
        if instance.id is not None: 
            qs = qs.exclude(pk=instance.pk)
        if qs.exists():
            raise forms.ValidationError("You already have an article with this title. Please change your title or delete your other post.")
        return title