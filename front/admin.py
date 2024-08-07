from django.contrib import admin
from .models import Article, ClientEmail, Request
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    fields = ('image', 'category', 'title', 'description', 'content')


class RequestAdmin(admin.ModelAdmin):
    model = Request
    list_display = ['subject', 'firstName', 'lastName', 'email', 'date', 'resolved']

admin.site.register(Article, ArticleAdmin)
admin.site.register(ClientEmail)
admin.site.register(Request, RequestAdmin)