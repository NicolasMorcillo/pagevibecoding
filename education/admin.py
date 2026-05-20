from django.contrib import admin
from .models import Curiosity, AIDefinition, Concept, NeuralNetworkType

@admin.register(Curiosity)
class CuriosityAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    search_fields = ('title', 'text')
    ordering = ('order', 'id')

@admin.register(AIDefinition)
class AIDefinitionAdmin(admin.ModelAdmin):
    list_display = ('author', 'order')
    search_fields = ('author', 'definition')
    ordering = ('order', 'id')

@admin.register(Concept)
class ConceptAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', 'description')

@admin.register(NeuralNetworkType)
class NeuralNetworkTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    search_fields = ('name', 'description', 'how_it_works')
    ordering = ('order', 'id')
