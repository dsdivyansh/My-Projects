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
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('post', 'author', 'text', 'created_date', 'approved_comment')
#     list_filter = ('approved_comment', 'created_date')
#     search_fields = ('author', 'text', 'created_date')
#     actions = ['approve_comments']
#
#     def approve_comments(self, request, queryset):
#         queryset.update(approved_comment=True)
# admin.site.register(Comment,CommentAdmin)
