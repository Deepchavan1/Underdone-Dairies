from django.shortcuts import render, HttpResponse, redirect
from poem.models import Poem, PoemComment
from django.contrib import messages
from django.contrib.auth.models import User
from poem.templatetags import extras

# Create your views here.


def poemHome(request):
    allPoems = []
    allPoems = Poem.objects.all()
    context = {'allPoems': allPoems}
    return render(request, "poem/poem.html", context)


def poemPost(request, slug):
    poem = Poem.objects.filter(slug=slug).first()
    poem.views = poem.views + 1
    poem.save()

    comments = PoemComment.objects.filter(post=poem, parent=None)
    replies = PoemComment.objects.filter(post=poem).exclude(parent=None)
    replyDict = {}
    for reply in replies:
      if reply.parent.sno not in replyDict.keys():
        replyDict[reply.parent.sno] = [reply]
      else:
        replyDict[reply.parent.sno].append(reply)

    context = {'poem': poem, 'comments': comments,'user': request.user, 'replyDict': replyDict}
    return render(request, "poem/poemPost.html", context)


def postComment(request):
    if request.method == "POST":
        comment = request.POST.get('comment')
        user = request.user
        postSno = request.POST.get('postSno')
        poem = Poem.objects.get(sno=postSno)
        parentSno = request.POST.get('parentSno')
        if parentSno == "":
            comment = PoemComment(comment=comment, user=user, post=poem)
            comment.save()
            messages.success( request, "Your comment has been posted successfully")
        else:
            parent = PoemComment.objects.get(sno=parentSno)
            comment = PoemComment(comment=comment, user=user, post=poem, parent=parent)
            comment.save()
            messages.success( request, "Your reply has been posted successfully")

    return redirect(f"/poem/{poem.slug}")
