from django.shortcuts import render, HttpResponse, redirect
from blog.models import Blog, BlogComment
from django.contrib import messages
from django.contrib.auth.models import User
from poem.templatetags import extras

# Create your views here.
def blogHome(request):
    allBlogs = []
    allBlogs = Blog.objects.all()
    context = {'allBlogs': allBlogs}
    return render(request, "blog/blog.html", context)


def blogPost(request, slug):
    blog = Blog.objects.filter(slug=slug).first()
    blog.views = blog.views + 1
    blog.save()

    comments = BlogComment.objects.filter(post=blog, parent=None)
    replies = BlogComment.objects.filter(post=blog).exclude(parent=None)
    replyDict = {}
    for reply in replies:
      if reply.parent.sno not in replyDict.keys():
        replyDict[reply.parent.sno] = [reply]
      else:
        replyDict[reply.parent.sno].append(reply)

    context = {'blog': blog, 'comments': comments,'user': request.user, 'replyDict': replyDict}
    return render(request, "blog/blogPost.html", context)


def postComment(request):
    if request.method == "POST":
        comment = request.POST.get('comment')
        user = request.user
        postSno = request.POST.get('postSno')
        post = Blog.objects.get(sno=postSno)
        parentSno = request.POST.get('parentSno')
        if parentSno=="":
            comment = BlogComment(comment=comment, user=user, post=post)
            comment.save()
            messages.success(
                request, "Your comment has been posted successfully")
        else:
            parent = BlogComment.objects.get(sno=parentSno)
            comment = BlogComment(comment=comment, user=user, post=post, parent=parent)
            comment.save()
            messages.success(
                request, "Your reply has been posted successfully")

    return redirect(f"/blog/{post.slug}")
