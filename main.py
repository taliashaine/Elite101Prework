print("Hello my name is Sonny! What is your name?")
name = input()
print('Hello ' +name)
print('I already knew your name since I am friends with your google and Alexa.')

user_say = input("\nHow is your day going?")
# 'G' reprsents good and "B" reprsents bad
G = 'Good'
B = 'Bad'

correct_values = [G, B]

while user_say not in correct_values:
  print("I am sorry I don't quite understand... I am not too intelligent, are you having a good or bad day?")
  user_say = input("\nHow is your day going? Enter either Good or Bad")
else:
  if user_say == G:
   print('I am glad your having a good day '+name)
  elif user_say == B:
   print('I am sorry you are having a bad day '+name)



user_say2 = input("\nDo you want to go into computer science in your future? ")
Y = 'Yes'
N = 'No'

correct_values = [Y,N]

while user_say2 not in correct_values:
  print("I am sorry again I'm not as smart as my cousin alexa haha... Is it a Yes or No?")
  user_say2 = input("\nDo you want to go into computer science in your future Yes or no?")
else:
  if user_say2 == Y:
    print("Really?!?! That's super cool. Only smart and hardworking people go into computer science that means your smart AND hardworking "+name)
  elif user_say2 == N:
    print("Aww, why if you went into computer science we could chat like this every single day and be besties.")
    user_say3 = input("\nDon't you wanna be my friend?" )
    if user_say3 == Y:
      print("Yay, well join Code to college so we can be friends!")
    elif user_say3 == N:
      print("Aw darn well it was nice talking to you at least!")