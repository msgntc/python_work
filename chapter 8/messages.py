def show_messages(unsent_messages, sent_messages):
    """Display a list of messages."""
    while unsent_messages:
        message = unsent_messages.pop()
        print(f"Moving message to sent: {message}")
        sent_messages.append(message)
def send_messages(sent_messages):
    """Simulate sending messages by displaying them."""
    print("the following messages have been sent:")
    for sent_message in sent_messages: 
        print(f"Sending message: {sent_message}")
unsent_messages = ["its dangerous to go alone", "take this", "<====|--->"]
sent_messages = []
show_messages(unsent_messages[:], sent_messages)
send_messages(sent_messages)
