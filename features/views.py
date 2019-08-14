from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from .models import Feature, Comment
from .forms import NewFeatureForm, NewCommentForm


# Create your views here.
def all_features(request):
    features= Feature.objects.all()
    features = sorted(features, key=lambda feature: feature.likes.count(), reverse=True)
    comments= Comment.objects.all()
    new_comment_form = NewCommentForm
    
    
    
    if request.method == "POST":
        new_comment_form = NewCommentForm(request.POST)
        feature = Feature.objects.get(id=request.POST["feature"])
        
        messages.success(request, "Your comment has been posted!")
        
        if new_comment_form.is_valid():
            
            
            
            instance = new_comment_form.save(commit=False)
            instance.feature = feature
            instance.author = request.user
            instance.save()
            
    
        
    return render(request,"features.html", {"features":features, "new_comment_form": new_comment_form, "comments":comments})
    
    
def NewFeature(request):
    
    if request.method == "POST":
        new_feature_form = NewFeatureForm(request.POST)
        messages.success(request, "Your feature has been posted!")
        
        if new_feature_form.is_valid():
            
            
            
            instance = new_feature_form.save(commit=False)
            instance.author = request.user
            instance.save()
            
            
    new_feature_form = NewFeatureForm()
    return render(request, 'new_feature.html', {"new_feature_form": new_feature_form})
    
    
    
def NewComment(request):
    
    if request.method == "POST":
        new_comment_form = NewCommentForm(request.POST)
        messages.success(request, "Your comment has been posted!")
        
        if new_comment_form.is_valid():
            
            
            
            instance = new_comment_form.save(commit=False)
            instance.author = request.user
            instance.save()
            
            
    new_comment_form = NewCommentForm()
    return render(request, 'add_comment.html', {"new_comment_form": new_comment_form})

def like_feature(request):
    feature = get_object_or_404(Feature, id=request.POST.get('feature_id'))
    messages.success(request, "Thank you for liking this feature, the features with the most likes will be worked on first!")
    feature.likes.add(request.user)
    return redirect(reverse('features'))