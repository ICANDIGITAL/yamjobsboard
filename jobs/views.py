import os
from django.shortcuts import render
from .api import fetch_jobs

def home(request):
    return render(request, 'jobs/home.html')

def search_jobs(request):
    api_key = os.getenv('SERPAPI_KEY')
    if not api_key:
        raise ValueError("API key not found. Please set the SERPAPI_KEY environment variable.")
    query = request.GET.get('query', '')
    location = request.GET.get('location', '')
    jobs = fetch_jobs(query, location, api_key) if query or location else []
    if query or location:
        jobs = fetch_jobs(query, location, api_key)
    context = {
        'jobs': jobs,
        'query': query,
        'location': location
    }
    return render(request, 'jobs/search.html', context)
print(os.getenv('SERPAPI_KEY'))
