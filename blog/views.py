from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import Article, Category
from django.shortcuts import get_object_or_404
from users.models import User

class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'
    context_object_name = 'articles'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = Article.objects.filter(status='published')
        
        # Category filtering
        if 'slug' in self.kwargs:
            queryset = queryset.filter(category__slug=self.kwargs['slug'])
            
        # Author filtering
        if 'username' in self.kwargs:
            queryset = queryset.filter(author__username=self.kwargs['username'])
            
        return queryset
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'slug' in self.kwargs:
            context['category'] = get_object_or_404(Category, slug=self.kwargs['slug'])
        if 'username' in self.kwargs:
            User = User
            context['author'] = get_object_or_404(User, username=self.kwargs['username'])
        return context
    
    def get(self, request, *args, **kwargs):
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            page = request.GET.get('page', 1)
            articles = self.get_queryset()
            paginator = Paginator(articles, self.paginate_by)
            
            try:
                articles = paginator.page(page)
            except:
                return JsonResponse({'has_next': False})
                
            article_html = render_to_string(
                'includes/article_list_items.html',
                {'articles': articles},
                request=request
            )
            
            return JsonResponse({
                'html': article_html,
                'has_next': articles.has_next()
            })
            
        return super().get(request, *args, **kwargs)

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_articles'] = Article.objects.filter(
            status='published',
            category=self.object.category
        ).exclude(id=self.object.id)[:2]
        return context