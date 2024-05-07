from serpapi import GoogleSearch

def fetch_jobs(query, location, api_key):
    params = {
        "engine": "google_jobs",
        "q": query,
        "location": location,
        "google_domain": "google.com",
        "api_key": api_key
    }
    client = GoogleSearch(params)
    results = client.get_dict()
    return results.get('jobs_results', [])