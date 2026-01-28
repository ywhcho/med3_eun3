from django.contrib import admin
from .models import Ingredient, Company, Efficacy, Medicine

# Register your models here.

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']
    ordering = ['name']


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'created_at']
    search_fields = ['name']
    ordering = ['name']


@admin.register(Efficacy)
class EfficacyAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']
    ordering = ['name']


@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ['name', 'company', 'approval_number', 'created_at']
    list_filter = ['company', 'created_at']
    search_fields = ['name', 'approval_number']
    filter_horizontal = ['ingredients', 'efficacies']
    ordering = ['-created_at']

