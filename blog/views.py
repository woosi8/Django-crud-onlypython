from django.shortcuts import render, redirect,get_object_or_404
from .models import Post
from .forms import PostForm

# Create your views here.

def main(request):
    posts=Post.objects # Post.object를 posts 변수에 담기
    return render(request, 'posts.html',{'posts':posts})

def create(request):
    #  사용자가 POST방식으로 request요청을 보내면 유효성 검증 뒤 내용 저장하고 main으로 돌아간다.
    if request.method=='POST':
        form=PostForm(request.POST) # form 변수에 PostForm 할당
        if form.is_valid(): #form 유효성 검증
            form.save()
            return redirect('main') # main페이지로 가기
    else:
        form =PostForm() # post 방식이 아니면 빈 form 열기
        # render할 때 post 객체를 생성하고 함께 보내준다.
        #  template(html)에서 호출할 내용들을 context(form) 부분에 dictionary 형태로 적어준다.
    return render(request,'create.html',{'form':form})

def detail(request,pk):
    post=get_object_or_404(Post, pk=pk)#해당 객체가 있으면 가져오고 없으면 404 에러, pk 로 pk 사용
    # django에서는 model통해 DB 생성 시 PK(기본키)를 자동으로 생성해준다!
    return render(request,'detail.html',{'post':post})

def update(request,pk):
    post=get_object_or_404(Post,pk=pk)
    if request.method=='POST':
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form=PostForm(instance=post)
    return render(request,'update.html',{'form':form})

def delete(request,pk):
    post=Post.objects.get(pk=pk)
    post.delete()#delete함수 실행
    return redirect('main')