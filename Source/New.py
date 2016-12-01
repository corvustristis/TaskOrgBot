from Strategy import BotStrategy
from time import sleep
from time import time
import datetime

articles = ['on', 'at', 'in']
days = {'Monday': 0, 
		'Tuesday': 1, 
		'Wednesday': 2, 
		'Thursday': 3, 
		'Friday': 4, 
		'Saturday': 6, 
		'Sunday': 7}

def get_unix_time(text):
	unix_time = -1
	if text[0] == 'on':
		task_day = days.get(text[0], -1)
		if day == -1:
			return unix_time
		cur_day = datetime.datetime.today().weekday()
		if task_day < cur_day:
			task_day += 7
		unix_time = (task_day - curr_day) * 3600 * 24 + int(time())
		return unix_time

	if text[0] == 'in':
		if len(text) == 3:
			if text[2] == 'hrs' or 'mins' or 'hr' or 'min':
				if text[2] == 'hrs' or 'hr':
					unix_time = int(text[1]) * 3600 + int(time())
				if text[2] == 'mins' or 'min':
					unix_time = int(text[1]) * 60 + int(time())
			return unix_time
		if len(text) == 5:
			if text[2] == ('hrs' or 'hr') and text[4] == ('mins' or 'min'):
				unix_time = int(text[1]) * 3600 + int(text[3]) * 60 + int(time())
	return unix_time

def check_msg(msg):
	text = msg.text.split()[1:]
	pos1 = 0
	pos2 = 0
	for i in range(len(text)):
		if text[i] in articles:
			pos1 = i
			break
	if pos1 == 0:
		return -1
	task = text[:pos1]
	for i in range(pos1, len(text)):
		if text[i] == 'with':
			pos2 = i
			break
	if pos2 == 0 or len(text) - pos2 != 3:
		return -1
	task_time = text[pos1 : pos2]
	unix_time = get_unix_time(task_time)
	if unix_time == -1:
		return -1
	if text[-1] != 'priority':
		return -1
	if text[-2] != 'high':
		if text[-2] != 'low':
			return -1
	f = open(str(msg.chat.id) + '.txt', 'a+')
	task_text = ''
	for i in task:
		task_text = task_text + i + ' '
	f.write(task_text)
	f.write(str(unix_time) + ' ')
	f.write(text[-2][0] + '\n')
	f.close()
	return unix_time	


class NewTask(BotStrategy):
	def __init__(self):
		pass
	
	def action(self, msg, bot):
		#if not check_msg(msg.text)
		unix_time = check_msg(msg)
		if unix_time <= 0:
			bot.send_message(msg.chat.id, "Message is wrong. Type /help for reference.")
			return
		else:
			bot.send_message(msg.chat.id, "Task is successfully added.")
		sleep(abs(unix_time - int(time())))
		p = 0
		text = msg.text.split()[1:]
		for i in range(len(text)):
			if text[i] in articles:
				p = i
				break
		task = text[:p]
		task_text = ''
		for i in task:
			task_text = task_text + i + ' '
		bot.send_message(msg.chat.id, "New reminder: " + task_text)
		f = open(str(msg.chat.id) + '.txt', 'r+')
		lines = f.readlines()
		for i in range(len(lines)):
			lines[i] = lines[i].split()
		for i in range(len(lines)):
			if (lines[i][-1] == text[-2][0]) and (lines[i][-2] == str(unix_time)):
				lines.remove(lines[i])
				break
		for i in range(len(lines)):
			lines[i] = ' '.join(lines[i]) + '\n'
		f.close()
		f = open(str(msg.chat.id) + '.txt', 'w')
		f.writelines(lines)
		f.close()
		