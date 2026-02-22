from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

class UserProfile(AbstractUser):
    user_photo = models.ImageField(null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    is_official = models.BooleanField(default=False)
    user_network = models.URLField()
    description = models.TextField()
    date_registered = models.DateField(auto_now_add=True)

class Follow(models.Model):
    following = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user1')
    follower = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user2')
    created_at = models.DateField(auto_now_add=True)

class City(models.Model):
    city_name = models.CharField(max_length=120)

class Hashtag(models.Model):
    hashtag_name = models.CharField(max_length=120)


class Post(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField()
    hashtags = models.ManyToManyField(Hashtag, blank=True)
    created_at = models.DateField(auto_now_add=True)


class PostContent(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.FileField()

class PostLike(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

class Review(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class ReviewLike(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)



