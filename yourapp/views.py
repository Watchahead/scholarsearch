from django.shortcuts import render

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
    return render(request, 'yourapp/search_results.html', {'results': results})
