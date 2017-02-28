from django.shortcuts import render_to_response
import models

# Create your views here.
def home(request):
    bbs_list = models.BBS.objects.all();
    return render_to_response('home.html',{'bbs_list':bbs_list})

def bbs_detail(request, bbs_id):
    bbs = models.BBS.objects.get(id=bbs_id)
    comment_list = models.Comment.objects.filter(bbs_id=bbs_id)
    return render_to_response("bbs_detail.html",{'bbs':bbs,'comment_list':comment_list,})

def login(request):

def regist(request):

def logout(request):


