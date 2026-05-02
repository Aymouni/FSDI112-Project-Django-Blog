from django.views.generic import (
    ListView
)
from .models import Post

# Create your views here.
# Class based view
class PostListView(ListView):
    # template_name is the attribue to render the html
    template_name = "posts/list.html"
    # model attribute let django know from which model (table) we want to retrieve data
    model = Post
    # context_object_name attribute allow us to change the variable on how we call it inside of templates
    context_object_name = "posts"

