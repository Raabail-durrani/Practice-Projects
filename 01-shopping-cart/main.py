foods = []
prices = []
total = 0


while True:
    food = input(" what do you want to buy(q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(" what is the price of food item:  $"))
        foods.append(food)
        prices.append(price)
        total = total + price
print(" YOUR CART  ")
for i in range(len(foods)):
    print("{}'s price is {}".format(foods[i],prices[i]))







        
        

