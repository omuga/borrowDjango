from celery import shared_task,Celery
import requests

app = Celery('tasks', backend='amqp',
broker='amqp://<userdjango>:<userdjango>@<127.0.0.1>/<userdjangohost>')
@shared_task
def verify_del_ids(id):
    r = requests.get('http://127.0.0.1:8081/api/users/validate/'+str(id))    
    return r.status_code
    

#celery -A borrowDomain worker --pool=solo -l info