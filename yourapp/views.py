from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
import requests
from django.shortcuts import render

def google_scholar_search(query):
    base_url = "https://serpapi.com/search"
    api_key = "2f18d17db4d6128578749cdd22492efdda164127477f279f286ccd081ea2eaa6"
    params = {"engine": "google_scholar", "q": query, "api_key": api_key}

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        results = response.json()
        return results
    else:
        return {"error": f"Error: {response.status_code}"}

def search_results(request):
    query = request.GET.get('q', '')
    results = google_scholar_search(query)
    print("Search results:", results)

    # Extract only the relevant search results (articles)
    articles = results.get('organic_results', [])

    # Configure the number of articles to display per page
    articles_per_page = 10

    # Create a Paginator object
    paginator = Paginator(articles, articles_per_page)

    # Get the current page number from the request's GET parameters
    page_number = request.GET.get('page')

    try:
        # Get the Page object for the current page
        page = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page
        page = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver last page
        page = paginator.page(paginator.num_pages)

    return render(request, 'yourapp/search_results.html', {'results': page, 'query': query})
