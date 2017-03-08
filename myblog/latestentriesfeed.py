from django.contrib.syndication.views import Feed
from django.urls import reverse
from myblog.newsItem import NewsItem


class LatestEntriesFeed(Feed):
    title = "Police beat site news"
    link = "/sitenews/"
    description = "Updates on changes and additions to police beat central."

    def items(self):
        return NewsItem.objects.order_by(NewsItem.event_date)[:5]

    def item_title(self, item):
        return NewsItem.event_title

    def item_description(self, item):
        return NewsItem.event_description

    def item_text(self):
        return NewsItem.text

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
        return reverse('news-item', args=[item.pk])
