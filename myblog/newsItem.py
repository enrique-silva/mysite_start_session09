from myblog.models import Post
from myblog.models import Category

class NewsItem():
    event_title = Post.title
    event_author = Post.author
    event_description = Category.description

    def __str__(self):
        return self.event_title