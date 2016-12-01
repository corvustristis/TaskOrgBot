from Strategy import BotStrategy

class DeleteTask(BotStrategy):
	def __init__(self):
		pass
	
	def action(self, chat_id, text, bot):
		bot.send_message(chat_id, "Task is successfully deleted.")
		