from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader
from .models import Album, Artist
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from album_manager.forms import AlbumForm, ArtistForm

def index(request):
    albums = Album.objects.order_by('year')
    artists = Artist.objects.order_by('name')
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'albums': albums}, request))

def album(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    template = loader.get_template('display_album.html')
    context = {
        'album': album
    }
    return HttpResponse(template.render(context, request))

def add_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('album_manager:index')
    else:
        form = AlbumForm()

    return render(request, 'album_form.html', {'form':form})


class CustomLoginView(LoginView):
    template_name="login.html"


def edit_album(request, id):
    album = get_object_or_404(Album, pk=id)
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect('album_manager:index')
    else:
        form = AlbumForm(instance=album)
        

    return render(request, 'album_form.html', {'form':form})


def delete_album(request, id):
    album = get_object_or_404(Album, pk=id)
    album.delete()
    return redirect("album_manager:index")

# Artist Section

def artist(request, artist_id):                                                                
    artist = get_object_or_404(Artist, pk=album_id)                                          
    template = loader.get_template('display_artist.html')                                       
    context = {                                                                                  
        'artist': artist                                                                       
    }                                                                                            
    return HttpResponse(template.render(context, request))                                       
def add_artist(request):                                                                        
    if request.method == 'POST':                                                                 
        form = ArtistForm(request.POST, request.FILES)                                          
        if form.is_valid():                                                                      
            form.save()                                                                          
            return redirect('album_manager:index')                                                     
    else:                                                                                        
        form = ArtistForm()                                                                     
                                                                                                 
    return render(request, 'artist_form.html', {'form':form})                                   
                                                                                                 
                                                                                                 
class CustomLoginView(LoginView):                                                                
    template_name="login.html"                                                                   
                         



def edit_artist(request, id):                                                                   
    album = get_object_or_404(Artist, pk=id)                                                  
    if request.method == 'POST':                                                                 
        form = ArtistForm(request.POST, request.FILES, instance=album)                        
        if form.is_valid():                                                                      
            form.save()                                                                          
            return redirect('album_manager:index')                                                     
    else:                                                                                        
        form = ArtistForm(instance=artist)                                                     
                                                                                                 
                                                                                                 
    return render(request, 'artist_form.html', {'form':form})                                   
                                                                                                 
def delete_artist(request, id):                                                                 
    artist = get_object_or_404(Artist, pk=id)                                                  
    artist.delete()                                                                             
    return redirect("album_manager:index")   

