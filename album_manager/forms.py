from django import forms
from .models import Artist, Album


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        widgets = {

                'name': forms.TextInput(attrs={'class': 'form-control'}),
                'genre': forms.Select(attrs={'class': 'form-control'}),
                'year': forms.TextInput(attrs={'class': 'form-control'}),
                'artist': forms.Select(attrs={'class': 'form-control'}),
                'picture': forms.ClearableFileInput(attrs={'class': 'form-control-file'})
                }

class ArtistForm(forms.ModelForm):                                                            
    class Meta:                                                                                 
        model = Artist
        fields = '__all__'                                                                      
        widgets = {                                                                             
                                                                                                
                'name': forms.TextInput(attrs={'class': 'form-control'}),                       
                'Country': forms.TextInput(attrs={'class': 'form-control'}),                     
                }   
