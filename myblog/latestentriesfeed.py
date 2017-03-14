from django.contrib.syndication.views import Feed
from django.urls import reverse
from myblog.models import Post


class LatestEntriesFeed(Feed):
    title = "Latest Posts"
    link = "/feed/"
    description = "The latest posts on the blog."

    def items(self):
        return Post.objects.order_by('-published_date')[:5]

    def item_title(self, item):
        return item.title

    def item_text(self, item):
        return item.text

    def item_author(self, item):
        return item.author

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item, **kwargs):
        return reverse('blog_detail', kwargs={'post_id': item.pk})
