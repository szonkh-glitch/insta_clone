from django_filters import FilterSet
from .models import PostLike

class PostLikeFilter(FilterSet):
    class Meta:
        model = PostLike
        fields = {
            'post': ['exact'],
            'user': ['exact'],
            'like': ['gt','lt'],
        }