print("Welcome to SKT System security Inc.")

code = input("\nEnter your code [1/2/3]:")

if code == "1":
  print("\nAccess Granted.")
  print("\nYou are using Member code.")
elif code == "2":

  print("\nAccess Granted.")
  print("\nYou are using officer Code.")
elif code == "3":
  print("\nAcess Granted.")
  print("\nYou are using VIP Code.")
else:
  print("\nIntruder! Invalid Code.")

input("\n\nPress the enter key exit.")