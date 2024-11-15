print("""Hello Good day!
How do you feel today?
Enter the answer by using the following:
Type H if you feel happy,
     F if you feel just fine,
     B if you feel bad today""")
mood = input("And you answer is: ")
if mood == "H":
  print("""
      _______________
      |             |
      |   o      o  |
      |             |
      |  \       /  |
      |   \_____/   |
      |_____________|""")
  print("\nRemember this feeling and thing about it when you feel sad.")
elif mood == "F":
  print("""
      _______________
      |             |
      |  o      o   |
      |             |
      |  _________  |
      |             |
      |_____________|""")
  print("Then prepare to face other feeling.")
elif mood == "B":
 print("""
      _______________
      |             |
      |   o      o  |
      |   _______   |
      |  /       \  |
      | /         \ |
      |_____________|
 keep in your mind that this is sign of something good that's gonna happen 
 something that good enough to make you happy or even  enough to be the best thing that ever happen to you.
 You just have to be strong wait for the time to rise then you will pass through it.""")


else:
  print("\nInvalid answer! You must feel crazy right now.")

input("\n\nPress the enter key to exit.")