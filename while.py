prompt = '\nPlease input ingredient of pizza.\n'
prompt += '\nEnter "quit" to end the procedure : \n'

message = ''

while message != 'quit' :
    message = input(prompt)
    if message != 'quit' :
       print(f'We will add {message} in your pizza.')
    else:
       break
   
print('\nMaking done!')
        

    

