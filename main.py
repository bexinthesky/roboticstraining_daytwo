# print 'Hello World'

# if 1 == 2 or 1 == 1:
#   print 'Hello'
# elif 1 == 1:
#   print 'Goodbye'

# def myFirstFunction(text):
#   print text
  
# myFirstFunction('Hello')

#Get the user's name
name = raw_input('Please Enter Your Name: ')

#Check user input to ensure that it is not an empty string
def validate_input(validate):
  if validate == ' ':
    return

# Start the game
def start_game():
  validate_input(name)
  print name + ' is here.'
  # other way to do string interpolation below
  #print '%s is here' %s (%name)




start_game()
  