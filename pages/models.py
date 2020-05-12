from django.db import models
from users.models import CustomUser
from django.urls import reverse


from .utils import urllizer


class UTM_source(models.Model):
    utm_url = models.CharField(verbose_name="Website URL", max_length=25)
    utm_source = models.CharField(
        verbose_name="Campaign Source", max_length=25, blank=True
    )
    utm_medium = models.CharField(
        verbose_name="Campaign Medium", max_length=25, blank=True
    )
    utm_campaign = models.CharField(
        verbose_name="Campaign Name", max_length=25, blank=True
    )
    utm_term = models.CharField(verbose_name="Campaign Term", max_length=25, blank=True)
    utm_content = models.CharField(
        verbose_name="Campaign Content", max_length=25, blank=True
    )
    utm_user = models.ForeignKey(
        CustomUser, verbose_name="User", on_delete=models.CASCADE
    )

    created_on = models.DateTimeField(verbose_name="Created", auto_now_add=True)
    updated_on = models.DateTimeField(verbose_name="Updated", auto_now=True)

    class Meta:
        verbose_name = "URL"
        verbose_name_plural = "URLs"
        ordering = ["created_on"]

    def build_link(self):
        if self.utm_url.endswith("/"):
            self.utm_url = f"{self.utm_url}"[0:-1]

        utm_tags = {
            "utm_source": self.utm_source,
            "utm_medium": self.utm_medium,
            "utm_campaign": self.utm_campaign,
            "utm_term": self.utm_term,
            "utm_content": self.utm_content,
        }
        utm_link_tags = []
        for key, value in utm_tags.items():
            if value:
                utm_link_tags.append(f"{key}={urllizer(value)}")
        return f"{self.utm_url}/?{'&'.join(utm_link_tags)}"

    def __str__(self):
        return self.build_link()

    def get_absolute_url(self):
        return reverse("link_details", args=[str(self.id)])
