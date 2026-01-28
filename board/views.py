from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Post

# Create your views here.

def list_view(request):
    """게시판 목록 뷰"""
    posts_list = Post.objects.all()
    page_number = request.GET.get('page', 1)
    
    # 페이지네이션 (10개씩)
    paginator = Paginator(posts_list, 10)
    page_obj = paginator.get_page(page_number)
    
    context = {
        'posts': page_obj.object_list,
        'page_obj': page_obj,
    }
    
    return render(request, 'board/list.html', context)


def detail_view(request, pk):
    """게시글 상세 뷰"""
    post = get_object_or_404(Post, pk=pk)
    
    # 조회수 증가
    post.views += 1
    post.save()
    
    context = {
        'post': post,
    }
    
    return render(request, 'board/detail.html', context)


@login_required
def create_view(request):
    """게시글 작성 뷰"""
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        
        post = Post.objects.create(
            title=title,
            content=content,
            author=request.user
        )
        
        return redirect('board:detail', pk=post.id)
    
    return render(request, 'board/form.html')


@login_required
def update_view(request, pk):
    """게시글 수정 뷰"""
    post = get_object_or_404(Post, pk=pk)
    
    # 작성자만 수정 가능
    if request.user != post.author:
        return redirect('board:detail', pk=pk)
    
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        
        return redirect('board:detail', pk=pk)
    
    context = {
        'post': post,
    }
    
    return render(request, 'board/form.html', context)


@login_required
def delete_view(request, pk):
    """게시글 삭제 뷰"""
    post = get_object_or_404(Post, pk=pk)
    
    # 작성자만 삭제 가능
    if request.user == post.author and request.method == 'POST':
        post.delete()
        return redirect('board:list')
    
    return redirect('board:detail', pk=pk)

