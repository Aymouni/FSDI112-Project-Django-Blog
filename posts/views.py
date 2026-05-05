from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post
from django.contrib.auth.models import User
from django.urls import reverse_lazy

# Create your views here.
# Class based view
class PostListView(ListView):
    # template_name is the attribue to render the html
    template_name = "posts/list.html"
    # model attribute let django know from which model (table) we want to retrieve data
    model = Post
    # context_object_name attribute allow us to change the variable on how we call it inside of templates
    context_object_name = "posts"

class PostDetailView(DetailView):           # GET Request -> Single element (Object)
    template_name = "posts/detail.html"
    model = Post
    context_object_name = "single_post"

class PostCreateView(CreateView):           # Post Request -> empty form (HTML)
    template_name = "posts/new.html"
    model = Post
    # Fields attribute is a list that allow us to enable/disable the inputs to render in the html
    fields = ["title", "subtitle", "body"]

    def form_valid(self, form):
        form.instance.author = User.objects.last()
        return super().form_valid(form)
    
class PostUpdateView(UpdateView):           # POST Request -> filled from (HTML)
    template_name = "posts/edit.html"
    model = Post
    fields = ["title", "subtitle", "body"]

class PostDeleteView(DeleteView):
    template_name = "posts/delete.html"
    model = Post
    # success_url attribute allow is to redirect the user if the request 
    success_url = reverse_lazy("post_list")