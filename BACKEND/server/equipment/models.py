from django.db import models

class EquipmentUpload(models.Model):
    name = models.CharField(max_length=200)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    summary = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.name