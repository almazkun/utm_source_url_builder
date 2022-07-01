from django.contrib.auth import get_user_model
from django.db import models

from utm.utils import urllizer


class Link(models.Model):
    creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    url = models.CharField(verbose_name="Website URL", max_length=254)
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

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def full_url(self):
        url = self.url

        if url.endswith("/"):
            url = url[:-1]

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
        return f"{url}/?{'&'.join(utm_link_tags)}"
