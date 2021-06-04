from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from .models import albums , tracks ,artists ,list

def view_genre(request):
    objs = albums.objects.all()
    return render(request,'genre.html',{'albums': objs})
    

# Create your views here.
def index(request):

    objs = albums.objects.all()                              #(SELECT * FROM albums)
    return render(request,'index.html',{'albums': objs})

def view_track(request,pk = None):
    if pk is not None:

        myalbum = get_object_or_404(albums, pk = pk)         #(SELECT * FROM tracks,albums WHERE track.album_id = albums.album_id )
        objs = tracks.objects.filter(album=myalbum.id)
        return render(request,'tracks.html',{'tracks':objs})
    
def all_tracks(request):
    objs = tracks.objects.all()                              #(SELECT * FROM tracks)
    return render(request,'tracks.html',{'tracks':objs})

def view_albums(request,pk = None):                          #(SELECT  * FROM albums,artists WHERE album.artist_id=artist.artist_id)
    objs = albums.objects.filter(artist = pk)
    return render(request,'albums.html',{'albums':objs})

def view_artists(request):
    
    objs = artists.objects.all()
    return render(request,'artists.html',{'artists':objs})


def search(request):
    if request.method == 'POST':
        albumtitle = request.POST.get('atitle')                         #(select * from albums where album.title= userinputtitle)
        try:
            status = albums.objects.filter(album_title = albumtitle)
        except:
            status = None
        return render(request,'albums.html',{'albums':status})

    else:
        messages.info(request,'no matching album found')
        return redirect('search')


def search_artists(request):                                                #(select * from artists where artists.artist_name = userinputname)
    if request.method == 'POST':
        aname = request.POST.get('a_name')
        try:
            status = artists.objects.filter(artist_name = aname)
        except:
            status = None
        return render(request,'artists.html',{'artists':status})

    else:
        messages.info(request,'no matching artist found')
        return render(request,'artists.html',{})

def search_track(request):
    if request.method == 'POST':
        tname = request.POST.get('ttitle')
        try:
            status = tracks.objects.filter(track_title = tname)
        except:
            status = None
        return render(request,'tracks.html',{'tracks':status})

    else:
        messages.info(request,"no matching track found")
        return redirect('search_track')

@login_required
def add_to_list(request,pk):                                                            #(Insert into list values(user_id=request.user,track_id=tracks.track_id))
    track = get_object_or_404(tracks,pk=pk)
    lists,created = list.objects.get_or_create(user_id=request.user,track_id = track)
    return redirect('view_list')

def view_list(request):
    objs = list.objects.filter(user_id=request.user)
    return render(request,'mylist.html',{'songs':objs})

def remove_from_list(request,pk):
    obj =  get_object_or_404(list,pk=pk)
    obj.delete()
    return redirect('view_list')