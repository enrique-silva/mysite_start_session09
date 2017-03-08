from myblog.models import Post
from myblog.models import Category



class NewsItem(Post):
    event_title = Post.title
    event_author = Post.author
    event_description = Category.description
    text = Post.text
    event_date = Post.created_date

