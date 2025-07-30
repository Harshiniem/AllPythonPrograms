print(''' Menu
      1. Indian
      2. Mexican
      3. Italian ''')
customer = int(input("sir, tell me which cuisine you need:"))
if customer == 1:
    print("Take right for Indian cuisine")
elif customer == 2:
    print("Take left for Mexican cuisine")
elif customer == 3:
    print("go straight for Italian cuisine")
else:
    print("Sorry for the inconvinence please wait for few minutes.")