from django.db import models

# Create your models here.
class Receiver(models.Model):
    
    received_json = models.TextField()
    created_on = models.DateTimeField(verbose_name="Created", auto_now_add=True)
    updated_on = models.DateTimeField(verbose_name="Updated", auto_now=True)


    def __str__(self):
        return received_json[:10]


    def get_absolute_url(self):
        return reverse("link_details", args=[str(self.id)])


    class Meta:
        db_table = ''
        managed = True
        verbose_name = "API_call"
        verbose_name_plural = "API_calls"
        ordering = ["created_on"]