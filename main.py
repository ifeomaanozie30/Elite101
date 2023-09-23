#I was not entirely sure what happened to my console and it would not let me see what exactly I was coding when used to work.
def user_name():
 #user_name()
 print('Hello! I am your chatbot')
 user_name = input('What is your name?\n')
 return 

def user_age():
  #user_name()
  user_name = input('Hi! Nice to meet you {}. How old are you?'.format(user_name))

def display_options():
  print('\nHow can I assist you today?'.format(user_name))
  print('1. Provide information')
  print('2. Ask a question')
  print('3. Exit')

  while True:
    display_options()
    choice = input('Please select 1, 2, or, 3')
    if choice == '1':
      print("You have selected 'Provide information'.")
      #Add code for whatever information they might need
    elif choice == '2':
      print("You have selected 'Ask a question.'")
      #Add code to ask what their question is and then answer it
    elif choice == '3':
      print("Bye!{} Please come again soon!" .format(user_name))
      break
      #Only used if the user wants to leave
    else:
     print("I'm sorry that's not a choice, Please select 1, 2, or 3.")

    
    
  

 



