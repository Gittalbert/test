from django.shortcuts import render,get_object_or_404,redirect
from one.models import Post

from .models import Comment
from .forms import CommentForm

# Create your views here.

def post_comment(request,post_pk):
    #获取文章，不存在报404
    post = get_object_or_404(Post,pk=post_pk)
    #用户请求为POST才处理表单数据
    if request.method == 'POST':
        
        form = CommentForm(request.POST)
        # 当调用 form.is_valid() 方法时，Django 自动帮我们检查表单的数据是否符合格式要求。
        if form.is_valid():
            
            comment = form.save(commit=False)
            #关联评论和文章
            comment.post = post
            # 最终将评论数据保存进数据库，调用模型实例的 save 方法
            comment.save()
            return redirect(post)
        else:
            comment_list = post.comment_set.all()
            context = {'post':post,'form':form,'comment_list':comment_list}
            return render(request,'detail.html',context=context)
    return redirect(post)

