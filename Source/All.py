import Strategy

class AllTasks(Strategy.BotStrategy):
	def __init__(self):
		pass
	
	def action(self, chat_id, bot):
		bot.send_message(chat_id, "All tasks: ")
