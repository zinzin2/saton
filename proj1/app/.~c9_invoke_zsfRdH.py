from django.shortcuts import render

# Create your views here.


def main(request):
    
    return render(request,'first/main.html')

    
def myprofile(request):
    return render(request,'first/myprofile.html')
    
    
def create(request):
    form = PostForm()
    return render(request, 'first/create.html', {'form': form})
   
def detail(request):
    return render(request, 'first/detail.html')
    
    

  






  