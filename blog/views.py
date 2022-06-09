from audioop import reverse
from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from blog.models import Category, Post, Comment
from .forms import PostForm,EditForm,CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
#def home(request):
    #return render(request, 'home.html', {})

class HomeView(ListView):
    model=Post
    template_name ='home.html'
    ordering=['-date']

    def get_context_data(self, *args, **kwargs):
        cat_menu=Category.objects.all()
        context=super(HomeView, self).get_context_data(*args,**kwargs)
        context["cat_menu"] = cat_menu
        return context

class Article_DetailView(DetailView):
    model =Post
    template_name='detail.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu=Category.objects.all()
        context=super(Article_DetailView, self).get_context_data(*args,**kwargs)

        stuff=get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        liked=False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked=True

        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context
class Addview(CreateView):
    model=Post
    form_class=PostForm
    template_name='addpost.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu=Category.objects.all()
        context=super( Addview, self).get_context_data(*args,**kwargs)
        context["cat_menu"] = cat_menu
        return context
class UpdatePostView(UpdateView):
    model=Post
    form_class=EditForm
    template_name='update.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu=Category.objects.all()
        context=super( UpdatePostView, self).get_context_data(*args,**kwargs)
        context["cat_menu"] = cat_menu
        return context
    #fields=['title','title_tag','body']

class DeletePostView(DeleteView):
    model=Post
    template_name='delete.html'
    success_url= reverse_lazy('home')   
    def get_context_data(self, *args, **kwargs):
        cat_menu=Category.objects.all()
        context=super(DeletePostView, self).get_context_data(*args,**kwargs)
        context["cat_menu"] = cat_menu
        return context
class CategoryView(CreateView):
    model=Category
    #form_class=PostForm
    fields = '__all__'
    template_name='category.html'
    def get_context_data(self, *args, **kwargs):
        cat_menu=Category.objects.all()
        context=super(CategoryView, self).get_context_data(*args,**kwargs)
        context["cat_menu"] = cat_menu
        return context
def Categorys(request,cats):
    category_posts=Post.objects.filter(category=cats.replace('-',' '))
    
    return render(request,'categories.html',{'cats':cats.title().replace('-',' '), 'category_posts' : category_posts })
    


      
  
def Like(request ,pk):
    post = Post.objects.get(id=pk)
    if post.likes.filter(id=request.user.id).exists(): 
        post.likes.remove(request.user)
        liked=False
    else:
        post.likes.add(request.user)
        liked =True

    return HttpResponseRedirect(reverse('detail', args=[str(pk)]))

class CommentView(CreateView):
    model=Comment
    form_class=CommentForm
    template_name='comment.html'
    

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'pk': self.kwargs['pk']})









# Create your views here.
