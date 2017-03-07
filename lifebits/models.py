from django.db import models
from django.core.urlresolvers import reverse

class User(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    email = models.EmailField(unique=True)
    handle = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('user', kwargs={"handle": self.handle})

class List(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    user = models.ForeignKey(User)
    
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('list', kwargs={"slug": self.slug})

    class Meta:
        ordering = ["-created_at"]

class Item(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField()
    favorited = models.IntegerField()
    ITEM_OPEN = 'OP'
    ITEM_IN_PROGRESS = 'IP'
    ITEM_DONE = 'DN'
    STATUS_CHOICES = (
        (ITEM_OPEN, 'Open'),
        (ITEM_IN_PROGRESS, 'In Progress'),
        (ITEM_DONE, 'Done!'),
    )
    status = models.CharField(max_length=2,
                              choices=STATUS_CHOICES,
                              default=ITEM_OPEN)
    completion = models.DateTimeField()
    ilist = models.ForeignKey(List)

    class Meta:
        ordering = ["-created_at"]

class Post(models.Model):
    IMG = 'IM'
    TEXT = 'TX'
    TYPE_CHOICES = (
        (IMG, 'Image'),
        (TEXT, 'Text'),
    )
    post_type = models.CharField(max_length=2,
                                 choices=TYPE_CHOICES,
                                 default=TEXT)
    content_image = models.ImageField(blank = True, upload_to='postimgs')
    content_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    item = models.ForeignKey(Item)

    class Meta:
        ordering = ["-created_at"]
