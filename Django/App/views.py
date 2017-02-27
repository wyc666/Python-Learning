from django.shortcuts import render_to_response
import models

# Create your views here.
def home(response):
    bbs_list = models.BBS.objects.all();
    return render_to_response('home.html',{'bbs_list':bbs_list})

def bbs_detail(response, bbs_id):
    bbs = models.BBS.objects.get(id=bbs_id)
    return render_to_response("bbs_detail.html",{'bbs':bbs})
