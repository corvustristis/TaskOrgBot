import config
import telebot
from Start import StartCommand
from Help import HelpCommand
from New import NewTask
from All import AllTasks
from Delete import DeleteTask

bot = telebot.TeleBot(config.token)

comms = ['start', 'help', 'new', 'all', 'delete']
st = StartCommand()
hp = HelpCommand()
nw = NewTask()
al = AllTasks()
dl = DeleteTask()

@bot.message_handler(content_types=["text"])
def msg_check(msg):
	if msg.text[0] != "/":
		bot.send_message(msg.chat.id, "Send me a command.")
		return
	
	comm = msg.text.split()[0][1:]
	if comm not in comms:
		bot.send_message(msg.chat.id, "Wrong command. Type /help for reference.")
		return
	
	if comm == 'start':
		st.action(msg.chat.id, bot)
		return
	
	if comm == 'help':
		hp.action(msg.chat.id, bot)
		return
	
	if comm == 'new':
		nw.action(msg, bot)
		return
	
	if comm == 'all':
		al.action(msg.chat.id, bot)
		return
	
	if comm == 'delete':
		dl.action(msg.chat.id, msg.text, bot)
	
	
if __name__ == '__main__':
	bot.polling(none_stop = True)	
	