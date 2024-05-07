import logging
from serpapi import search

logger = logging.getLogger(__name__)

def fetch_jobs(query, location, api_key):
    params = {
        "engine": "google_jobs",
        "q": query,
        "location": location,
        "api_key": api_key
    }

    try:
        results = search(params)
        return results.get('jobs_results', [])
    except Exception as e:
        error_message = "Failed to fetch job listings: {}".format(str(e))
        if hasattr(e, 'response') and e.response is not None:
            error_message += ", API Response: {}".format(e.response.text)
        logger.error(error_message)
        return []

