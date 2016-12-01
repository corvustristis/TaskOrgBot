from Strategy import BotStrategy

class HelpCommand(BotStrategy):
	def __init__(self):
		pass
	
	def action(self, chat_id, bot):
		bot.send_message(chat_id, """Type /new and your task, eg.:
			  /new watch new episode of Supergirl on Monday with high priority
			  /new Sara throws party at 18:00 with low priority
			  /new i need to feed cat in 8 hrs 10 mins with high priority.
And when time comes, you'll get a message from me.
To view all tasks type /all and /delete, if some task is unnecessary. You can type /delete only after /all.""")
		