# basic python below
# print 'Hello World'

# simple if statement below
# if 1 == 2 or 1 == 1:
#   print 'Hello'
# elif 1 == 1:
#   print 'Goodbye'

# simple function below
# def myFirstFunction(text):
#   print text

# calling simple function below  
# myFirstFunction('Hello')


# Get the user's name (variable)
name = raw_input('Please Enter Your Name: ')

#Check user input to ensure that it is not an empty string (in a function)
def validate_input(validate):
  if validate == ' ':
    return

# Start the game (in a function)
def start_game():
  validate_input(name)
  print name + ' is here.'
  # other way to do string interpolation below
  #print '%s is here' %s (%name)

# execute function
start_game()
  