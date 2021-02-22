# Create your tasks here
import json
import requests

from bs4 import BeautifulSoup
from celery import shared_task
from .models import Progress


@shared_task
def create_new_object():
    Progress.objects.all().delete()
    response = requests.get('https://www.sololearn.com/Profile/5737049')
    soup = BeautifulSoup(response.text, 'html.parser')

    progressed = soup.find_all('script')
    progressed = list(progressed)
    progressed = str(progressed[7])[29:-10]
    progressed = json.loads(progressed)

    for i in progressed['getProfile']['coursesProgress']:
        data = float(i['progress']) * 100
        Progress(data=data).save()





