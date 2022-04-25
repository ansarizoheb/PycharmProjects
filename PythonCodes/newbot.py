from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.updater import Updater
from telegram.update import Update
updater = Updater("5208653196:AAEk8G2XC_Tl45o3D0WRkhthqlyH_XiS9ns",
                  use_context=True)
def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Hello sir, Welcome to the Bot.Please write\
        /help to see the commands available.")
def help(update: Update, context: CallbackContext):
        update.message.reply_text("""Available Commands :- 
 /youtube - To get the youtube URL 
 /linkedin - To get the LinkedIn profile URL 
 /gmail - To get gmail URL 
 /geeks - To get the GeeksforGeeks URL""")
def gmail_url(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Gmail Link => \
    https://www.gmail.com/)")
def youtube_url(update: Update, context: CallbackContext):
    update.message.reply_text("Youtube Link =>\
    https://www.youtube.com/")
def linkedIn_url(update: Update, context: CallbackContext):
        update.message.reply_text(
            "LinkedIn URL => \
    https://www.linkedin.com/in/dwaipayan-bandyopadhyay-007a/")
def geeks_url(update: Update, context: CallbackContext):
        update.message.reply_text(
            "GeeksforGeeks URL => https://www.geeksforgeeks.org/")
def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)
def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)
def sample_responses(input_text):
        user_message = str(input_text).lower()
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('youtube', youtube_url))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('linkedin', linkedIn_url))
updater.dispatcher.add_handler(CommandHandler('gmail', gmail_url))
updater.dispatcher.add_handler(CommandHandler('geeks', geeks_url))
# updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
# updater.dispatcher.add_handler(MessageHandler(
#     Filters.command, unknown))  # Filters out unknown commands
# Filters out unknown messages.
# updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))
updater.start_polling()