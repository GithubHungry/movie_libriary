from django.contrib import admin

from . import models

# Register your models here.
admin.site.register(models.Category)
admin.site.register(models.Genre)
admin.site.register(models.Movie)
admin.site.register(models.MovieShots)
admin.site.register(models.Actor)
admin.site.register(models.Rating)
admin.site.register(models.RatingStar)
admin.site.register(models.Reviews)
