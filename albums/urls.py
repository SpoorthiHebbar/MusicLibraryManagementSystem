from django.contrib import admin
from django.urls import path , include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('',views.index,name="index"),
    path(r'^view_track-(?P<pk>[0-9]+)',views.view_track,name = "view_track"),
    path(r'^view_albums-(?P<pk>[0-9]+)',views.view_albums,name = "view_albums"),
    path('all_tracks',views.all_tracks,name="all_tracks"),
    path('view_artists',views.view_artists,name = "view_artists"),
    path('search_artists',views.search_artists,name="search_artists"),
    path('search_track',views.search_track,name="search_track"),
    path('search',views.search,name="search"),
    path('view_genre',views.view_genre,name="view_genre"),
    path(r'^add_to_list-(?P<pk>[0-9]+)',views.add_to_list,name = "add_to_list"),
    path(r'^remove_from_list-(?P<pk>[0-9]+)',views.remove_from_list,name = "remove_from_list"),
    path('view_list',views.view_list,name = "view_list"),
    path('admin/', admin.site.urls),
    url(r'^download/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT})
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
