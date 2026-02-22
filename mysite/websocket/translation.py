from .models import (UserProfile, Follow, City, Hashtag, Post,
                     PostLike, PostContent, Review, ReviewLike)
from modeltranslation.translator import TranslationOptions,register

@register(UserProfile)
class CategoryTranslationOptions(TranslationOptions):
    fields = ()

@register(Follow)
class CategoryTranslationOptions(TranslationOptions):
    fields = ()

@register(City)
class CategoryTranslationOptions(TranslationOptions):
    fields = ()

@register(Hashtag)
class CategoryTranslationOptions(TranslationOptions):
    fields = ()

@register(Post)
class CategoryTranslationOptions(TranslationOptions):
    fields = ()

@register(PostLike)
class CategoryTranslationOptions(TranslationOptions):
    fields = ()

@register(PostContent)
class CategoryTranslationOptions(TranslationOptions):
    fields = ()

@register(Review)
class CategoryTranslationOptions(TranslationOptions):
    fields = ()

@register(ReviewLike)
class CategoryTranslationOptions(TranslationOptions):
    fields = ()