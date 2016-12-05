from Strategy import BotStrategy

class StartCommand(BotStrategy):
	def __init__(self):
		pass
	
	def action(self, num, bot):
		bot.send_message(num, """I'm here to organize your tasks. 
Simply type /new and your task, eg.:
			  /new go to dentist on Monday with high priority
			  /new Sara throws party at 18:00 with low priority
			  /new i need to feed cat in 8 hrs 10 mins with high priority.
And when time comes, you'll get a message from me.
To view all tasks type /all and /delete, if some task is unnecessary. You can type /delete only after /all.
Type /help for reference.""")
		name = str(num)+".txt"
		file = open(name, "w")
		file.close()