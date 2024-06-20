from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.utils.html import format_html

from netflixApp.models import Movie
from netflixApp.models import Category
from netflixApp.models import Tag

admin.site.register(Category)
admin.site.register(Tag)


class MovieAdmin(admin.ModelAdmin):

    def preview(self, movie):
        """Render preview image as html image."""

        return format_html(
            f'<img style="height: 200px" src="/media/{movie.preview_image}" />'
        )

    def video(self, movie):
        """Render movie video as html image."""

        return format_html(
            f"""
            <video width="320" height="240" controls>
                <source src="/media/{movie.file}" type="video/mp4">
                Your browser does not support the video tag.
            </video>"""
        )

    preview.short_description = 'Movie image'
    video.short_description = 'Movie video'
    list_display = ['name', 'preview', 'video', 'description']

admin.site.register(Movie, MovieAdmin)