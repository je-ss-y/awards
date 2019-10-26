from django.shortcuts import render
import datetime as dt
from django.http  import HttpResponse,Http404

# Create your views here.





def posts_of_day(request):
    date = dt.date.today()
    return render(request, 'all-posts/poststoday.html', {"date": date,})