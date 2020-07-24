from django.db import models

# Create your models here.


class Blog(models.Model):
    objects = models.Manager()
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=255, unique=True)
    body = models.TextField()
    summery = models.CharField(max_length=100, null=True)
    pub_date = models.DateTimeField(db_index=True, auto_now_add=True)
    category = models.ForeignKey('blog.Category', on_delete=models.CASCADE)


class Category(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title
