from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.views.generic import View
from blog.forms import SignupForm,post_form,CommentForm
from blog.models import Post,Comment
from django.views.generic import View,TemplateView,ListView,DetailView,DeleteView,UpdateView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.urls import reverse_lazy



@login_required
def post_list_view(request):
    post_list=Post.objects.all()
    paginator=Paginator(post_list,3)
    page_number=request.GET.get('page')
    try:
        post_list=paginator.page(page_number)
    except PageNotAnInteger:
        post_list=paginator.page(1)
    except EmptyPage:
        post_list=paginator.page(paginator.num_pages)
    return render(request,'blog/viewasblogg.html',{'post_list':post_list})



# def post_detail(request):
#     comments = Comment.objects.filter(approved_comment=True)
#     new_comment = None
#     # Comment posted
#     if request.method == 'POST':
#         comment_form = CommentForm(data=request.POST)
#         if comment_form.is_valid():
#
#             # Create Comment object but don't save to database yet
#             new_comment = comment_form.save(commit=False)
#             # Assign the current post to the comment
#             new_comment.comments = comments
#             # Save the comment to the database
#             new_comment.save()
#     else:
#         comment_form = CommentForm()
#
#     return render(request,"blog/comment.html", {
#                                            'comments': comments,
#                                            'new_comment': new_comment,
#                                            'comment_form': comment_form})



def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

def post_detail_view(request):
    return render(request,'blog/post_detail.html')



class Post_Detail(DetailView):
    model=Post # object name = book or object

class Post_Detail_Crud(DetailView):
    model=Post
    template_name='blog/Post_Detail_Crud.html'

# def delete_new(request):
#     return redirect('Post_Detail_Crud.html')
#     return render(request,'blog/post_confirm_delete.html')


def logout_view(request):
    logout(request)
    return redirect(request,'blog/home.html')

def base_view(request):
        return render(request,'blog/home.html')

def Home_view(request):
        return render(request,'blog/home.html')

class delete_view(DeleteView):
    model=Post

    success_url= reverse_lazy('home')
    template_name='blog/post_confirm_delete.html'
    # post=Post.objects.get(id=id)
    # post.delete()
    # return redirect('/home')

# def update_view(request,pk,template_name='blog/update.html'):
#
#     pst=Post.objects.get(pk=pk)
#     if request.method == "POST":
#         form=post_form(request.POST,instance=pst)
#         if form.is_valid():
#             form.save()
#         return redirect('/')
#     return render(request,template_name,{'pst':pst})

class update_view(UpdateView):
    model=Post
    fields=('title','body')
    def get_success_url(self):
        request=self.request
        return('/')
    # success_url=reverse_lazy('/')

# @login_required
# def Admin_blog(request):
#     return render(request,'blog/admin_blog.html')

@login_required
def PostBlog_view(request):
    form=post_form()
    if request.method == "POST":
        form=post_form(request.POST)
    if form.is_valid():
        form.save()
    return render(request,'blog/PostBlog.html',{'form':form})

@login_required
def My_post(request):
    name=request.user
    post_list=Post.objects.filter(author=name)
    return render(request,'blog/my_post.html',{'post_list':post_list})




def SignupForm_view(request):
    form=SignupForm()
    if request.method == "POST":
        form = SignupForm(request.POST)
    if form.is_valid():
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'blog/signup_form.html',{'form':form })
