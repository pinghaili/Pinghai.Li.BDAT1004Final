import requests
from .models import Job  

def fetch_jobs():
    app_id = '86f12d76'
    app_key = '513866e30fd4f984afc4b508c596b82b'
    path = 'https://api.adzuna.com/v1/api/jobs/'  # The URL from which you're fetching data
    country = 'ca'
    results_per_page = 100
    
    url = f'{path}{country}/search/6?app_id={app_id}&app_key={app_key}&results_per_page={results_per_page}'
    response = requests.get(url)
    response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code

    jobs_data = response.json()

    for job_entry in jobs_data['results']:
        print(job_entry['company']['display_name'])

        job = Job(
            id=job_entry['id'],
            title=job_entry['title'],
            description=job_entry['description'],
            company=job_entry['company']['display_name'],
            country=job_entry['location']['area'][0],
            adref=job_entry['adref'],
            created=job_entry['created'],
            redirect_url=job_entry['redirect_url'],
            contract_time=job_entry.get('contract_time'),
            contract_type=job_entry.get('contract_type', None),
            salary_is_predicted=job_entry['salary_is_predicted'],
            salary_min=job_entry.get('salary_min', None),
            salary_max=job_entry.get('salary_max', None),
            category=job_entry['category']['label'],
            latitude=job_entry.get('latitude', 0.0),
            longitude=job_entry.get('longitude', 0.0),
        )
        job.save()

# If this script is run directly, call fetch_jobs()
if __name__ == '__main__':
    fetch_jobs()