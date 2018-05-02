pyg = 'ay' #suffix

original = raw_input('Enter a word:') #input from user

if len(original) > 0 and original.isalpha(): #validate if not empty with only alphabetical characters(string)
  word = original.lower() #convert all to lower case
  first = word[0] #select the 1st letter from the input
  new_word = word + first + pyg #create the translated string along with the suffix
  new_word = new_word[1:len(new_word)] #slice the 1st character
  print new_word
else:
    print 'empty'