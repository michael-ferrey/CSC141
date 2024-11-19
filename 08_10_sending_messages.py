def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(messages):
    sent_messages = []  
    while messages:
        message = messages.pop(0) 
        print(message)
        sent_messages.append(message)  
    return sent_messages

text_messages = ["Hello, how is your day going?", "Remeber we have meetings today!","It's so good to see you!","Great job at practice today!","Have a good rest of your day!"]


sent_messages = send_messages(text_messages)


print("\nText Messages:", text_messages)
print("Sent Messages:", sent_messages)
