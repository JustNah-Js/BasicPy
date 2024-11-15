name = input("Hello! What's your name: ")
print("Hi!", name)
sin = int(input("How old are you?"))
if sin >= 0 and sin <= 6 :
  print("Your are baby")
elif sin >= 7 and sin <= 12 :
  print("You are too young")

elif sin >= 13 and sin <= 19 :
  print("You are Teenager")
elif sin >= 20 and sin <= 29 :
  print("You are Young Adult")
elif sin >= 30 and sin <= 49 :
  print("You are Adult")
elif sin >= 50 and sin <= 70 :
  print("You are old")
elif sin >= 80 and sin <= 90 :
  print("You are too you")
else:
  print("Your age are unbeliveable")


input("\n\nPress the enter key to exit.")