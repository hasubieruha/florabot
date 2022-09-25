from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

TELEGRAM_TOKEN = 5773970516:AAET3OrtXekCnaqv1bcXLE8xXlTWeIWCyU0
updater = Updater(TELEGRAM_TOKEN, use_context=True)

# Reply Text

def start(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Siapa yang Flora?")

#Reply Video
def floranime(update: Update, context: CallbackContext):
	update.message.reply_video(
		"https://github.com/hasubieruha/florabot/blob/main/video/floranime.mp4")


# Error Command

def unknown(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Maaf nih kak, '%s', command ini tidak tersedia, mohon dicek melalui tautan yang ada di command /help" % update.message.text)

def unknown_text(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Kata yang dikirim adalah '%s', untuk command harus menggunakan / di depannya" % update.message.text)


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('contoh', contoh))

# Filters out unknown commands
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))

# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()
