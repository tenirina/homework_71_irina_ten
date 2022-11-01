from django.contrib import admin

from posts.models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'image', 'count_like', 'count_comment', 'created_at')
    list_filter = ('id', 'description', 'created_at')
    search_fields = ('id', 'description', )
    fields = ('id', 'description', 'image', 'count_like', 'count_comment', 'created_at')
    readonly_fields = ('id', 'count_like', 'count_comment', 'created_at')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'text', 'post', 'created_at')
    list_filter = ('id', 'post', 'created_at')
    search_fields = ('id', 'author')
    fields = ('id', 'author', 'text', 'post', 'created_at')
    readonly_fields = ('id', 'author')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
