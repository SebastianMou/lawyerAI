from django.contrib import admin
from django.contrib.auth.models import User

from .models import ContractProject, AIHighlightChat

# Register your models here.
admin.site.register(ContractProject)
admin.site.register(AIHighlightChat)