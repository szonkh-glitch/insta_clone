from django.contrib import admin
from .models import (UserProfile, Follow, City, Hashtag, Post,
                     PostLike, PostContent, Review, ReviewLike)
from modeltranslation.admin import TranslationAdmin, TranslationInlineModelAdmin


class PostContentInline(admin.TabularInline, TranslationInlineModelAdmin):
    model = PostContent
    extra = 1

@admin.register(Post)
class PostAdmin(TranslationAdmin):
    inlines = [PostContentInline]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

admin.site.register(UserProfile)
admin.site.register(Follow)
admin.site.register(City)
admin.site.register(Hashtag)
admin.site.register(PostLike)
admin.site.register(Review)
admin.site.register(ReviewLike)

