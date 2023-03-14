from django.contrib import admin
from .models import Articles, Comments

# Register your models here.


class CommentInline(admin.TabularInline):
    model = Comments
    extra = 0

class ArticleInline(admin.ModelAdmin):
    inlines = [CommentInline,
               ]


admin.site.register(Articles, ArticleInline)
admin.site.register(Comments)
