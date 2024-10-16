from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class ContractProject(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = HTMLField(blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contract_project', null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        # Return a default string if name is None
        return self.name if self.name else "Unnamed Contract Project"

    class Meta:
        verbose_name_plural = 'Contract Projects'
        ordering = ('-created_at',)

class AIHighlightChat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    highlighted_text = models.TextField()
    instruction = models.TextField()
    ai_response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    contract_project = models.ForeignKey(ContractProject, on_delete=models.CASCADE, related_name='ai_chats')

    class Meta:
        verbose_name_plural = 'AI Highlight Chats'
        ordering = ('-created_at',)

