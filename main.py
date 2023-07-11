print("Welcome to the Rollercoaster!")
height = int(input("How tall are you, in cm? "))

if height >= 120:
  age = int(input(f"You are {height}cm tall; how old are you? "))
  photo = input(f"Would you like a £3 photo ticket? Yes or No ")
  if age >= 18: 
    ticketPrice = 12
  elif age >= 12:
    ticketPrice = 10
  else:
    ticketPrice = 8
  
  if photo == "Yes":
    ticketPrice += 3
  
  print(f"You are {age}; The ticket is £{ticketPrice}, enjoy the ride.")
  
else:
  print(f"You are {height}cm tall; you are not permitted to ride the Rollercoaster, have a nice day.")
  exit()