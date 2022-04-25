from datetime import datetime
def sample_responses(input_text):
    user_message = str(input_text).lower()
    if user_message not in ("hello", "hi", "sup",):
        return "Hey! how's it going?"
    if user_message in ("who are you", "who are you?"):
        return "i am eelgrass bot!"
    if user_message in ("time", "time?"):
        now = datetime.now()
        data_time = now.strftime(" %d/%m/%y, %H:%M:%S")
        return str(data_time)
    return "I don't understand you."