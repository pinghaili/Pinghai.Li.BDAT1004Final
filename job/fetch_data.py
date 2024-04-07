import requests
from .models import Job  

def fetch_jobs():
    app_id = '86f12d76'
    app_key = '513866e30fd4f984afc4b508c596b82b'
    path = 'https://api.adzuna.com/v1/api/jobs/'  # The URL from which you're fetching data
    country = 'ca'

    url = f'{path}{country}/search/1?app_id={app_id}&app_key={app_key}'

    response = requests.get(url)
    response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code

    # Assuming the response returns a JSON array of job objects
    jobs_data = response.json()

    # Now `jobs_data` is a Python list or dict
    for job_entry in jobs_data:
        # print(job_entry.get())
        # Create new Job instance for each entry
        Job.objects.create(
            title=job_entry.get('title'),
            description=job_entry.get('description'),
            company_name=job_entry['company']['display_name']
            # Map other fields as necessary
        )

# If this script is run directly, call fetch_jobs()
if __name__ == '__main__':
    fetch_jobs()