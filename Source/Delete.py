from Strategy import BotStrategy
from time import time

def print_all(chat_id, bot):
	f = open(str(chat_id) + '.txt', 'r+')
	lines = f.readlines()
	for i in range(len(lines)):
		lines[i] = lines[i].split()

	important = []
	unimportant = []
	urgent = []
	nonurgent = []
	for line in lines:
		if line[-1] == 'h':
			important.append(' '.join(line) + '\n')
		if line[-1] == 'l':
			unimportant.append(' '.join(line) + '\n')
	cur_time = int(time())
	for line in lines:
		if int(line[-2]) <= (cur_time + 12 * 3600):
			urgent.append(' '.join(line) + '\n')
		if int(line[-2]) > (cur_time + 12 * 3600):
			nonurgent.append(' '.join(line) + '\n')
	for line in lines:
		line = ' '.join(line) + '\n'
	number = 1
	msg = "Here is a list of all your tasks:\n\nImportant/Urgent:\n"
	for line in important:
		if line in urgent:
			msg += str(number) + '. ' + line[0:-13] + '\n'
			number += 1
	msg += '\nImportant/Nonurgent:\n'
	for line in important:
		if line in nonurgent:
			msg += str(number) + '. ' + line[0:-13] + '\n'
			number += 1
	msg += '\nUnimportant/Urgent:\n'
	for line in unimportant:
		if line in urgent:
			msg += str(number) + '. ' + line[0:-13] + '\n'
			number += 1
	msg += '\nUnimportant/Nonurgent:\n'
	for line in unimportant:
		if line in nonurgent:
			msg += str(number) + '. ' + line[0:-13] + '\n'
			number += 1

	bot.send_message(chat_id, msg)


class DeleteTask(BotStrategy):
	def __init__(self):
		pass
	
	def action(self, chat_id, text, bot):
		try:
			num = int(text[7:])
		except ValueError:
			bot.send_message(chat_id, "You gave wrong number.")
			return
		
		f = open(str(chat_id) + '.txt', 'r+')
		lines = f.readlines()
		f.close()
		for i in range(len(lines)):
			lines[i] = lines[i].split()
		
		important = []
		unimportant = []
		urgent = []
		nonurgent = []
		for line in lines:
			if line[-1] == 'h':
				important.append(line)
			if line[-1] == 'l':
				unimportant.append(line)
		cur_time = int(time())
		for line in lines:
			if int(line[-2]) <= (cur_time + 12 * 3600):
				urgent.append(line)
			if int(line[-2]) > (cur_time + 12 * 3600):
				nonurgent.append(line)
		all_tasks = []
		
		for line in important:
			if line in urgent:
				all_tasks.append(line)
		for line in important:
			if line in nonurgent:
				all_tasks.append(line)
		for line in unimportant:
			if line in urgent:
				all_tasks.append(line)
		for line in unimportant:
			if line in nonurgent:
				all_tasks.append(line)
		if num > len(all_tasks):
			bot.send_message(chat_id, "You gave wrong number.")
			return
		all_tasks.remove(all_tasks[num - 1])
		f = open(str(chat_id) + '.txt', 'w')
		for line in all_tasks:
			line = ' '.join(line) + '\n'
			f.write(line)
		f.close()
		bot.send_message(chat_id, "Task is successfully deleted.")
		
		print_all(chat_id, bot)		
		