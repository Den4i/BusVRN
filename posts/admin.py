from django.contrib import admin

# Register your models here.

from .models import Post


class PostUpAdmin(admin.ModelAdmin):
    list_display = ["title", "timestamp"]
    list_filter = ["timestamp"]
    search_fields = ["title", "content"]
    list_editable = ['title']

    class Meta:
        model = Post

admin.site.register(Post, PostUpAdmin)