from django.views.generic import ListView, DetailView, DeleteView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import post
from django.urls import reverse_lazy
#new
from django.views.generic.edit import FormMixin
from .forms import CommentForm
# Create your views here.

class BlogListView(ListView):
    model = post
    template_name = 'home.html'    


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = post
    template_name = 'new_post.html'
    fields = ['title', 'author', 'body']
    
class BlogDetailView(FormMixin, DetailView):
    model = post
    template_name = 'post_detail.html'
    form_class = CommentForm

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk':self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()
        if 'form' not in context:
            context['form'] = self.get_form()
        return context    

    def post (self, request, *args, **kwargs): #post the get us the comment, checks if the form is valid, checks the 
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = self.request.user
        comment.author = self.object
        comment.save()
        return super().form_valid(form)           

class BlogUpdateView(UpdateView):    
    model = post 
    template_name = 'post_edit.html'
    fields = ['title', 'body']

class BlogDeleteView(DeleteView):
    model = post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

class profileBlogListView(LoginRequiredMixin, ListView):
    model = post
    template_name ='profile.html'

    def get_queryset(self):
        all_posts = Post.objects.all()
        filtered_post = post.objects.filter(author = self.request.user)
        return filtered_post