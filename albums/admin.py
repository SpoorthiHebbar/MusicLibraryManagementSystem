

# Register your models here.
from django.contrib import admin
from .models import albums,tracks,list,artists
# Register your models here.
admin.site.register(albums)
admin.site.register(tracks)
admin.site.register(list)
admin.site.register(artists)