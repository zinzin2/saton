from django.shortcuts import render, get_object_or_404, redirect
##from ../details/models.py import Details
from details.models import Details


def main(request):
    competition_detail = Details.objects.filter(post_type=1)
    study_detail = Details.objects.filter(post_type=2)
    IT_detail = Details.objects.filter(post_type=3)
    return render(request,'front/main.html', {'competition_detail':competition_detail, 'study_detail':study_detail, 'IT_detail':IT_detail})
    
def myprofile(request):
    return render(request,'front/myprofile.html')
    
    
def create(request):
    ##form = PostForm()
    if request.method == 'POST':
        title = request.POST.get('title')
        user_name = request.POST.get('user_name')
        user_num = request.POST.get('user_num')
        content = request.POST.get('content')
        post_type = request.POST.get('post_type')
        detail=Details(title=title, user_name=user_name, user_num=user_num, content=content, post_type=post_type)
        detail.save()
        return redirect('main')
        
    return render(request, './front/writing.html')
    
   
def detail(request, detail_id):
    detail = get_object_or_404(Details, pk=detail_id)
    return render(request, 'front/page1.html', {'detail': detail})
    
def register(request):
    return render(request, './login_app/signup.html')

def login(request):
    return render(request, './login_app/login.html')

def logout(request):
    return render(request, './front/main.html')
    
def create_competition(request):
    ##form = PostForm()
    if request.method == 'POST':
        title = request.POST.get('title')
        user_name = request.POST.get('user_name')
        user_num = request.POST.get('user_num')
        content = request.POST.get('content')
        detail=Details(title=title, user_name=user_name, user_num=user_num, content=content)
        detail.save()
        return redirect('main')
        
    return render(request, './front/writing.html')
    
    
def create_event(request):
    ##form = PostForm()
    if request.method == 'POST':
        title = request.POST.get('title')
        user_name = request.POST.get('user_name')
        user_num = request.POST.get('user_num')
        content = request.POST.get('content')
        detail=Details(title=title, user_name=user_name, user_num=user_num, content=content)
        detail.save()
        return redirect('main')
        
    return render(request, './front/writing.html')
    
    
def edit(request, id):
    detail = Details.objects.get(pk= id)
    return render(request, './front/writing.html',{'detail':detail})
    
    
def update(request, id):
    if request.method == 'POST':
        detail = Details.objects.get(pk= id)
        title = request.POST.get('title')
        user_name = request.POST.get('user_name')
        user_num = request.POST.get('user_num')
        content = request.POST.get('content')
        detail.title = title
        detail.user_name = user_name
        detail.user_num = user_num
        detail.content = content
        detail.save()
    return redirect('detail',detail.id)

    
def delete(request, del_detail_id):
    delete_detail = get_object_or_404(Details, pk=del_detail_id)
    delete_detail.delete()
    return redirect('main')
    
# def page1(request, detail_id):
#     detail = get_object_or_404(Details, pk = detail_id)
#     return render(request, 'front/page1.html', {'detail':detail})
    