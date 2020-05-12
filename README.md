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