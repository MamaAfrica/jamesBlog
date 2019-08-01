from django.shortcuts import render, get_object_or_404,redirect
from django.shortcuts import HttpResponseRedirect
from .models import Post
from .models import Trend
# Create your views here.


def index(request):
    posts = Post.objects.all().exclude(visibility='Drafted')
    trends = Trend.objects.all().exclude(visibility='Drafted')
    return render(request, "index.html", {'posts': posts, 'trends': trends})

def detail(request, slug):
    post = get_object_or_404(Post, slug=slug, visibility="Published")
    return render(request, "details.html", {'post': post,})
def detailTrend(request, slug):
    trend = get_object_or_404(Trend, slug=slug, visibility="Published")
    return render(request, "detailsTrend.html", {'trend': trend})
#def female(request, slug):
 #   trend = get_object_or_404(Trend, slug=slug, visibility="Published")
  #  return render(request, "femaleWears.html", {'trend': trend})
def advert(request):
    return render(request,"advert.html",{})
def about(request):
        return render(request, "about.html", {})
#def add_comment(request, slug):
#    post=get_object_or_404(Post, slug=slug)
    #  if request.method=="POST":
    #   form=CommentForm(request.POST or None)
    #   if form.is_valid():
    #       comment=form.save(commit=False)
    #       comment.post=post
    #       comment.save()
    #       return redirect(request,'details/<str:slug>/', slug=post.slug)
    #   else:
    #       form=CommentForm()
    #       template='add_comment.html'
    #       context={'form':form}
    #       return render(request,template,context)