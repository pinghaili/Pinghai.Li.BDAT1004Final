# from background_task import background
from .fetch_data import fetch_jobs

# @background(schedule=600)
def fetch_data_task():
    print("======= fetch_jobs ======")
    # fetch_jobs()