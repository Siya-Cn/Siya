texts = ['hello','bye','sorry','thanks']

#def show_messages(texts):
   # while texts:
       # one_text = texts.pop()
        #print(one_text)

#show_messages(texts)

sent_message = []
def send_message(texts,sent_message):
    while texts:
        current_message = texts.pop()
        sent_message.append(current_message)
        print(texts)
        print(sent_message)

send_message(texts,sent_message)
