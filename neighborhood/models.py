from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from tinymce.models import HTMLField
import datetime as dt

# Create your models here.


class Neighborhood(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    occupants_count = models.IntegerField()
    pub_date = models.DateTimeField(auto_now_add=True)
    Admin = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)

    def save_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def get_neighborhoods(cls):
        projects = cls.objects.all()
        return projects

    @classmethod
    def search_neighborhoods(cls, search_term):
        projects = cls.objects.filter(name__icontains=search_term)
        return projects

    @classmethod
    def get_by_admin(cls, Admin):
        projects = cls.objects.filter(Admin=Admin)
        return projects

    @classmethod
    def get_neighborhood(request, Neighborhood):
        try:
            project = Neighborhood.objects.get(pk=id)

        except ObjectDoesNotExist:
            raise Http404()

        return project

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'My Neighborhood'
        verbose_name_plural = 'Neighborhoods'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    photo = models.ImageField(
        upload_to='profile_pics/', blank=True, default='profile_pics/default.jpg')
    neighborhood = models.ForeignKey(
        Neighborhood, on_delete=models.CASCADE, blank=True, default='1')

    def save_profile(self):
        self.save()

        img = Image.open(self.photo.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.photo.path)

    def delete_profile(self):
        self.delete()

    def __str__(self):
        return f"{self.user}, {self.bio}, {self.photo}"

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'


class Business(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    pub_date = models.DateTimeField(auto_now_add=True)
    Admin = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    admin_profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, blank=True, default='1')
    address = models.TextField()
    neighborhood = models.ForeignKey(
        Neighborhood, on_delete=models.CASCADE, blank=True, default='1')

    def save_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def get_allbusiness(cls):
        business = cls.objects.all()
        return business

    @classmethod
    def search_business(cls, search_term):
        business = cls.objects.filter(name__icontains=search_term)
        return business

    @classmethod
    def get_by_neighborhood(cls, neighborhoods):
        business = cls.objects.filter(
            neighborhood__name__icontains=neighborhoods)
        return business

    @classmethod
    def get_businesses(request, id):
        try:
            business = Business.objects.get(pk=id)

        except ObjectDoesNotExist:
            raise Http404()

        return business

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'My Business'
        verbose_name_plural = 'Business'


class Posts(models.Model):
    post = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    author_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    @classmethod
    def get_allpost(cls):
        posts = cls.objects.all()
        return posts

    @classmethod
    def get_by_neighborhood(cls, neighborhoods):
        posts = cls.objects.filter(neighborhood__name__icontains=neighborhoods)
        return posts

    def __str__(self):
        return self.post

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'My Post'
        verbose_name_plural = 'Posts'
