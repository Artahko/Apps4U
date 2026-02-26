from django.contrib import admin
from .models import Petition, Vote
# Register your models here.

@admin.register(Petition)
class PetitionAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at', 'user')

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('petition', 'user', 'value', 'created_at')
    list_filter = ('value', 'created_at')
