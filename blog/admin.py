from django.contrib import admin
from blog.models import Post, Tag, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = [
		'title',
	]
	raw_id_fields = ['author', 'likes','tags']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
	list_display = [
		'title',
	]
	raw_id_fields = ['posts']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	list_display = [
		'text',
		'author',
		'post',
	]
	raw_id_fields = ['post', 'author']
