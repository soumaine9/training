from django.shortcuts import render
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
#from .forms import ImageForm, PostForm
#from .models import Images

# Create your views here.


@login_required
def post(request):
    posts = Post.objects.all()

    form = PostForm(request.POST, request.FILES)

    if form.is_valid():
        new_post = form.save(commit=False)
        new_post.user=request.user
        new_post.save()

        for f in files:
            img = Image(image=f)
            image.save()
            new_post.image.add(img)
        new_post.save()

    context = {
        'post_list':posts,
        'form':form,
    }
    return render(request, 'index.html', {'postForm':postForm, 'formset':formset})
        