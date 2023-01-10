import time
# Chatbot that responds according to the user's input

print("Welcome to Houston Eats")
decision = input("What would you like to know off our restaurant? 1 for Resorvations, 2 to Start your order: ")

if decision == "1":#Reservations
  reserve = input("When would you like a resorvation?")
  print("Great, your reservation has been saved to " +reserve+". See you then!")
elif decision == "2":#Start order
  order = input("Heres our menu: 1. Burger 2. Tacos 3. Salad: ")
  if order == "1":#They chose a Burger
    print("Your Burger is coming soon!")
    time.sleep(3)
    print("Here your burger is ready, enjoy")
  elif order == "2":#They chose Tacos
    print("Your Tacos are coming soon!")
    time.sleep(3)
    print("Your Tacos are ready, here you go enjoy!")
  elif order == "3":#They chose Salad
    print("Your Salad will be here soon")
    time.sleep(3)
    print("Your Salad is here and ready! Enjoy!")
  else:
    print("Not on the Menu, hahaha")
else:#Didnt pick 1 or 2
  print("Not a option")
