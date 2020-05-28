from django.contrib import admin
from blog.models import Post,Comment


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=['title','slug','author','publish','created','updated','status']
    list_filter=('status','author','publish')
    search_fields=('title','body')
    prepopulated_fields={'slug':('title',)}
admin.site.register(Post,PostAdmin)
admin.site.register(Comment)

