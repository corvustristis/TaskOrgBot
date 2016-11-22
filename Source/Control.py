import config
import telebot
import Start
import Help
import New
import All
import Delete

bot = telebot.TeleBot(config.token)

comms = ['start', 'help', 'new', 'all', 'delete']
st = Start.StartCommand()
hp = Help.HelpCommand()
nw = New.NewTask()
al = All.AllTasks()
dl = Delete.DeleteTask()

@bot.message_handler(content_types=["text"])
def msg_check(msg):
	if msg.text[0] != "/":
		bot.send_message(msg.chat.id, "Send me a command.")
		print(msg.from_user.username + ": " + msg.text)
		return
	
	comm = msg.text.split()[0][1:]
	if comm not in comms:
		bot.send_message(msg.chat.id, "Wrong command. Type /help for reference.")
		print(msg.from_user.username + ": " + msg.text)
		return
	
	if comm == 'start':
		st.action(msg.chat.id, bot)
		print(msg.from_user.username + ": " + msg.text)
		return
	
	if comm == 'help':
		hp.action(msg.chat.id, bot)
		print(msg.from_user.username + ": " + msg.text)
		return
	
	if comm == 'new':
		nw.action(msg.chat.id, msg.text, bot)
		print(msg.from_user.username + ": " + msg.text)
		return
	
	if comm == 'all':
		al.action(msg.chat.id, bot)
		print(msg.from_user.username + ": " + msg.text)
		return
	
	if comm == 'delete':
		dl.action(msg.chat.id, msg.text, bot)
		print(msg.from_user.username + ": " + msg.text)
		return
	
	
if __name__ == '__main__':
	bot.polling(none_stop = True)	
	