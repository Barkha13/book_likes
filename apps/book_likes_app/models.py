from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now = True)
    updated_at = models.DateTimeField(auto_now_add = True)
    # liked_books = models.ManyToManyField(Book, related_name = "liked_users")
    def __str__(self):
        return "Users: ---,{} ----{}------{}".format(self.first_name, self.last_name, self.email)
    
class Book(models.Model):
    name = models.CharField(max_length = 255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    uploader = models.ForeignKey(User,related_name = "uploaded_books")
    liked_users = models.ManyToManyField(User, related_name = "liked_books")
    def __str__(self):
        return "Books: ---,{} ----{}----{}".format(self.name, self.desc, self.uploader_id)



    # def __repr__(self):
    #     return "Books: ---,{} ----{}".format(self.name, self.desc)

    