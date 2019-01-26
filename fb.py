#!/usr/bin/env python3
import time

from fbchat import Client
from fbchat.models import *

from credent import secret


def sendMessage(message):
	client = Client(secret["fb_login"], secret["fb_password"])
	#print('Own id: {}'.format(client.uid))

	thread_id = secret["fb_thread_id"]
	thread_type = ThreadType.GROUP

	time.sleep(5)
	# Will send a message to the thread
	client.send(Message(text=message), thread_id=thread_id, thread_type=thread_type)



#sendMessage("Bot: ")
#print('Own id: {}'.format(client.uid))

#client.send(Message(text='Hi me!'), thread_id=client.uid, thread_type=ThreadType.USER)

#client.logout()