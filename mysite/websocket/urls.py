from django.urls import path, include
from rest_framework import routers
from .views import( UserProfileViewSet, FollowAPIViewSet, CityAPIView, HashtagViewSet,
                    PostViewSet, PostContentViewSet, PostLikeViewSet,
                    ReviewViewSet, ReviewLikeViewSet, RegisterView, LoginView, LogoutView)

router = routers.DefaultRouter()
router.register(r'users', UserProfileViewSet, basename='profiles')
router.register(r'hashtags', HashtagViewSet)
router.register(r'posts', PostViewSet)
router.register(r'postcontents', PostContentViewSet)
router.register(r'postlikes', PostLikeViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'reviewlikes', ReviewLikeViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('follow/', FollowAPIViewSet.as_view()),
    path('city/', CityAPIView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('register/', RegisterView.as_view()),
]