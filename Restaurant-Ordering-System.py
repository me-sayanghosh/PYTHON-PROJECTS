#define the manue of the restaurant
menu = {
    'pizza' : 50,           #1
    'Pasta' : 40,           #2
    'Burger' : 50,          #3
    'Egg_Roll' : 40,        #4
    'Biriyani' : 150,       #5
    'Salad' : 50,           #6
    'Butter_Chiken' : 120,  #7
    'Mutton_Kosha' : 170,   #8
    'Momo' : 70,            #9
    'Chole_Bature' : 110,   #10
}
print("::::::::::::: WELLCOME TO MY RESTAURANT :::::::::::::")
print("Recipes of our restaurant :-")
print("pizza : 50;\nPasta : 40;\nBurger : 50;\nEgg_Roll : 40;\nBiriyani : 150;\nSalad : 50;\nButter_Chiken : 120;\nMutton_Kosha : 170;\nMomo : 70;\nChole_Bature : 110")   





order_total=0


item_1= input("Enter the name of the item you want to order = ")
if item_1 in menu:
    order_total = order_total=menu[item_1]
    print(f"Your item \"{item_1}\" has been added to your order")

else:
    print(f"Ordered item \"{item_1}\" is not available yet !!!")    


another_order = input("Do you want to add another item ? (Yes/No) ")    
if another_order == "Yes":
    item_2 = input("Enter the name of the second item = ")
    if item_2 in menu:
        order_total= order_total+menu[item_2]
        print(f"Item \"{item_2}\" has been added to your order")

    else:
        print(f"Item \"{item_2}\" is not available yet !!!")

print(f"The total ammount of ordered items to pay is :{order_total}")
