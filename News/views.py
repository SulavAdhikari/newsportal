# news/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import News
from .forms import NewsForm, NewsSearchForm
from deeplearning.sentiment import predict_text
from User.models import UserProfile

@login_required
def post_news(request):
    if not UserProfile.objects.filter(user=request.user).exists():
        return redirect('user_profile')

    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.author = request.user

            # sentiment 
            sentiment = predict_text(news.title)
            if sentiment == '-1':
                news.sentiment = "negative"
                print('set as negative')
            elif sentiment == '0':
                news.sentiment = "neutral"
                print('set as neutral')
            elif sentiment == '1':
                news.sentiment = "postive"
                print('set as positive')
            news.save()
            return redirect('news_list')
    else:
        form = NewsForm()
    return render(request, 'News/post_news.html', {'form': form})

def view_news(request, news_id):
    news = News.objects.get(id=news_id)
    return render(request, 'News/view_news.html', {'news': news})

def list_news(request):
    news_lists = News.objects.all()

     # Handle search
    search_form = NewsSearchForm(request.GET)
    if search_form.is_valid():
        query = search_form.cleaned_data['query']
        if query:
            news_lists = News.search(query)
    
    news_list = news_lists.filter(published=True)
    return render(request, 'News/list_news.html', {'news_list': news_list, 'search_form': search_form})
    # Update your news/templates/news/list_news.html to include the search bar:
