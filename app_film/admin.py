from django.contrib import admin
from app_film.model film import * 
from app_film.model genre import *

# Register your models here.
admin.site.Register(film)
admin.site.Register(genre)
