# robovac
Instructions:
1. run **pip install -r requirements.txt**
2. run **python manage.py runserver**
3. in a second terminal, change directory to rasachat and run **rasa train**, then run **rasa run -p 5500 --enable-api**
4. in a third terminal, change directory to rasachat and run **rasa run actions**
5. visit http://127.0.0.1:8000/
