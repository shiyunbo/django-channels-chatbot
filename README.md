# Django Channels Websocket Chatbot
A Django chatbot that is capable of doing math and searching Chinese poet online. Developed with django, channels, celery and redis using websocket technology. All dependencies are given in requirements.txt.

This project includes two apps:
1. chat:  online chat and group chat.
2. bots:  commands given to Celery via messages. Celery runs the background tasks and delivers back the results to channels once the tasks are completed.

## How to run this project
```python
git clone https://github.com/shiyunbo/django-channels-chatbot/
cd myproject
pip install requirements.txts

python manage.py migrate
python manage.py runserver

# windows
Celery -A myproject worker -l info -P eventlet

# Linux
Celery -A myproject worker -l info
```
Note：This project depends on redis. Please ensure it has been installed properly. 
