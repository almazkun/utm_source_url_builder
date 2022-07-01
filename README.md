# link to demo: [https://utm.akun.dev/](https://utm.akun.dev/?utm_source=GitHub&utm_campaign=GitHub)


# Collect campaign data with custom URLs
### Add parameters to URLs to identify the campaigns that refer traffic.

By adding campaign parameters to the destination URLs you use in your ad campaigns, you can collect information about the overall efficacy of those campaigns, and also understand where the campaigns are more effective. For example, your Summer Sale campaign might be generating lots of revenue, but if you're running the campaign in several different social apps, you want to know which of them is sending you the customers who generate the most revenue. Or if you're running different versions of the campaign via email, video ads, and in-app ads, you can compare the results to see where your marketing is most effective.

When a user clicks a referral link, the parameters you add are sent to Analytics, and the related data is available in the Campaigns reports.

## Parameters

There are 5 parameters you can add to your URLs:

* `utm_source`: Identify the advertiser, site, publication, etc. that is sending traffic to your property, for example: google, newsletter4, billboard.
* `utm_medium`: The advertising or marketing medium, for example: cpc, banner, email newsletter.
* `utm_campaign`: The individual campaign name, slogan, promo code, etc. for a product.
* `utm_term`: Identify paid search keywords. If you're manually tagging paid keyword campaigns, you should also use utm_term to specify the keyword.
* `utm_content`: Used to differentiate similar content, or links within the same ad. For example, if you have two call-to-action links within the same email message, you can use `utm_content` and set different values for each so you can tell which version is more effective.

Each parameter must be paired with a value that you assign. Each parameter-value pair then contains campaign-related information.

For example, you might use the following parameter-value pairs for your Summer Sale campaign:

`utm_source` = `summer-mailer` to identify traffic that results from your Summer Sale email campaign
`utm_medium` = `email` to identify traffic from the email campaign vs. the in-app campaign
`utm_campaign` = `summer-sale` to identify the overall campaign

If you used these parameters, your custom-campaign URL would be:

    https://www.example.com/?utm_source=summer-mailer&utm_medium=email&utm_campaign=summer-sale


More information: [Google support](https://support.google.com/analytics/answer/1033863?hl=en).
# link to demo: [https://utm.akun.dev/](https://utm.akun.dev/?utm_source=GitHub&utm_campaign=GitHub)


# Collect campaign data with custom URLs
### Add parameters to URLs to identify the campaigns that refer traffic.

By adding campaign parameters to the destination URLs you use in your ad campaigns, you can collect information about the overall efficacy of those campaigns, and also understand where the campaigns are more effective. For example, your Summer Sale campaign might be generating lots of revenue, but if you're running the campaign in several different social apps, you want to know which of them is sending you the customers who generate the most revenue. Or if you're running different versions of the campaign via email, video ads, and in-app ads, you can compare the results to see where your marketing is most effective.

When a user clicks a referral link, the parameters you add are sent to Analytics, and the related data is available in the Campaigns reports.

## Parameters

There are 5 parameters you can add to your URLs:

* `utm_source`: Identify the advertiser, site, publication, etc. that is sending traffic to your property, for example: google, newsletter4, billboard.
* `utm_medium`: The advertising or marketing medium, for example: cpc, banner, email newsletter.
* `utm_campaign`: The individual campaign name, slogan, promo code, etc. for a product.
* `utm_term`: Identify paid search keywords. If you're manually tagging paid keyword campaigns, you should also use utm_term to specify the keyword.
* `utm_content`: Used to differentiate similar content, or links within the same ad. For example, if you have two call-to-action links within the same email message, you can use `utm_content` and set different values for each so you can tell which version is more effective.

Each parameter must be paired with a value that you assign. Each parameter-value pair then contains campaign-related information.

For example, you might use the following parameter-value pairs for your Summer Sale campaign:

`utm_source` = `summer-mailer` to identify traffic that results from your Summer Sale email campaign
`utm_medium` = `email` to identify traffic from the email campaign vs. the in-app campaign
`utm_campaign` = `summer-sale` to identify the overall campaign

If you used these parameters, your custom-campaign URL would be:

    https://www.example.com/?utm_source=summer-mailer&utm_medium=email&utm_campaign=summer-sale


More information: [Google support](https://support.google.com/analytics/answer/1033863?hl=en).

```
from django.db import models
from users.models import CustomUser
from django.urls import reverse


from .utils import urllizer


class UTM_source(models.Model):
    utm_url = 
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


```