# Django Channels Websocket Chatbot
A Django chatbot that is capable of doing math and searching Chinese poet online. Developed with django, channels, celery and redis using websocket technology. All dependencies are given in requirements.txt.

This project includes two apps:
1. chat:  online chat and group chat.
2. bots:  commands given to Celery via messages. Celery runs the background tasks and delivers back the results to channels once the tasks are completed.
