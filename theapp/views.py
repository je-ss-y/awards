from django.shortcuts import render,redirect
import datetime as dt
from django.http  import HttpResponse,Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import PostForm
from .models import Snap
# Create your views here.




@login_required(login_url='/accounts/login/')
def posts_of_day(request):
    current_user = request.user
    date = dt.date.today()
    snap =  Snap.objects.all()

    # comment = Comment.objects.all()

    # for image in images:
    #     comments = Comment.objects.filter(image=image)
    #     print(comments)


    # comment = Comment.objects.filter(id = current_user.id).first()
    # print(comment)
    return render(request, 'all-posts/poststoday.html', {"date": date,"snap":snap})



@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            # post.user = current_user
            post.save()
        return redirect('postsToday')

    else:
        form = PostForm()
    return render(request, 'all-posts/newpost.html', {"form": form})

