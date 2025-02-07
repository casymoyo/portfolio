from django.shortcuts import render
from .forms import EmailForm
from .models import Email, Category, Portifolio
from django.views import View
from loguru import logger

class Index(View):
    form_class = EmailForm
    initial = {'key': 'value'}
    template_name = 'index.html'
    projects = Portifolio.objects.all()

    logger.info(f'Projects: {projects}')

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        print(self.projects)
        
        return render(request, self.template_name,
         {'form': form, 'projects':self.projects})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return render(request, self.template_name, {'form': form, 'projects':self.projects}) 
        else:
            logger.info('failed to save the form')

        return render(request, self.template_name, {'form': form, 'projects':self.projects})  