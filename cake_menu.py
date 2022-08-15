from cake import Cake

cakes = []

while True:
  print("Cake Menu")
  print("1: Add Cake")
  print("2: View Cake")
  print("3: Eat cake")
  cmd = int(input("> "))
  if cmd == 1:
    cakeType = input("Cake type: ")
    cakeSlices = int(input("Cake slices: "))
    cakes.append(Cake(cakeType, cakeSlices))
  if cmd == 2:
    print("which cake would you like to view?")
    for i in range(len(cakes)):
      print(str(i)+ ': ' + cakes[i].get_name())
    v = int(input("> "))
    print(cakes[v].get_description())
    #for obj in cakes:
      #print(obj.get_name())
  if cmd == 3:
    print("which cake to eat?")
    for i in range(len(cakes)):
      print(str(i)+ ': ' + cakes[i].get_name())
    c = int(input("> "))
    print("How many slices would you like?")
    num = int(input("> "))
    cakes[c].eat(num)
