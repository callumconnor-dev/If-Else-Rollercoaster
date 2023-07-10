print("Welcome to the Rollercoaster!")
height = int(input("How tall are you, in cm? "))

if height >= 120:
  age = int(input(f"You are {height}cm tall; how old are you? "))
  
  if age >= 18:
    print(f"You are {age}; The ticket is £14, enjoy the ride.")
  elif age >= 12:
    print(f"You are {age}; The ticket is £8, enjoy the ride.")
  else:
    print(f"You are {age}; You must be 12 or older to ride this ride.")
    exit()
  
else:
  print(f"You are {height}cm tall; you are not permitted to ride the Rollercoaster, have a nice day.")
  exit()