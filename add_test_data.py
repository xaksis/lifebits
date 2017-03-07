#!/home/hrishi/lifebits/bin/python
from lifebits.models import User
user = User(first_name='Hrishikesh',last_name='Bakshi',email='bakshi.hrishikesh@gmail.com',handle='hsbakshi')
user.save()
