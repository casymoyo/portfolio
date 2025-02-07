from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from users.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']
        
    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('blog:category_articles', kwargs={'slug': self.slug})
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        
    @property
    def article_count(self):
        return self.articles.filter(status='published').count()

class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='articles', null=True)
    content = models.TextField()
    featured_image = models.ImageField(upload_to='blog/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=10, 
        choices=[('draft', 'Draft'), ('published', 'Published')], 
        default='draft'
    )
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse('blog:article_detail', kwargs={'slug': self.slug})
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    @property
    def reading_time(self):
        words_per_minute = 200
        word_count = len(self.content.split())
        minutes = word_count / words_per_minute
        return max(1, round(minutes))