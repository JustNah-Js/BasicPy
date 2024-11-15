

nom = input("Please type your name: ")
hate = input("What is your favourite subject? ")
print("\nHi!", nom)
sin = int(input("Now enter your score from 0-50 in dis subject:"))
print("""___________________""")
print("""   score of""", hate)
print("""___________________\n""")
if sin <= 24:
  print("Poor")
elif sin >= 25 and sin <= 31 :
  print("Below average")

elif sin >= 32 and sin <= 36 :
  print("Average")
elif sin >= 37 and sin <= 42 :
  print("Good")
elif sin >= 43 and sin <= 47 :
  print("Very good")
elif sin >= 48 and sin <= 50 :
  print("Excellent")
else:
  print("Impossible kid")

input("\n\nPress the enter key to exit.")