from django.shortcuts import render, get_object_or_404, redirect
from .forms import TweetForm
from .models import Tweet

def index_view(request):
    return render(request, 'index.html')

def Tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweet_list.html', {'tweets': tweets})

def create_tweet(request):
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm()
    return render(request, 'tweet_form.html', {'form': form})

def Tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id)
    if request.method == 'POST':    
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm(instance=tweet)
    return render(request, 'tweet_form.html', {'form': form})

def Tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id)
    if request.method == 'POST':
        tweet.delete() 
        return redirect('tweet_list')
    return render(request, 'tweet_confirm_delete.html', {'tweet': tweet})
