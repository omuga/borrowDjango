from celery import shared_task,Celery
import requests
#@shared_task
#def verify_users_ids(id):
#    r = requests.get('http://127.0.0.1:8000/api/borrows/delete/'+str(id))   
#    return r.response 
app = Celery('tasks', backend = 'amqp',broker = 'amqp://userdjango:userdjango@http://127.0.0.1:5672/userdjangohost')

@shared_task
def add(x, y):
    return x + y

#celery -A userdomain worker --pool=solo -l info