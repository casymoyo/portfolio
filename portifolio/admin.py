from django.contrib import admin
from .models import Email, Category, Portifolio


@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Portifolio)
class PortifolioAdmin(admin.ModelAdmin):
    pass