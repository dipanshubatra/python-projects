import time
import sys
menu = {'pizza':30,
            'burger':20,
            'noodles':25,
            'coffee':7,
            'tea':10,
            'manchurian':50}
def animated_total(total):
    for i in range(1, int(total) + 1):
        print(f"\r🧾 Total Bill: ₹{i}", end='', flush=True)
        time.sleep(0.02)
    print()

def concessions():
    cart = []
    price = []
    total = 0

    while True: 
        print("\n1. MENU")
        print("2.  ORDER")
        print("3.  Exit ")
        take = input("Choose the option above ==>  ")
        if take.lower() == "menu" or take =='1':
            print("------------MENU------------")
            for i,j in menu.items():
                print(f"{i} - ₹{j}")
            print("-----------------------------") 
        elif take.lower() == 'order' or take == '2':
            while True:
                choice = input("😋Order the items from menu\n(or press x to exit)==>   \n").lower()
                if choice == 'x':
                    if cart == []:
                        print("YOUR CART🛒 IS EMPTY ARE YOU  NOT HUNGRY???")
                    else:
                        confirm = input("\nAre you sure to confirm order(y/n)")
                        if "y" in confirm.lower():
                            total =0
                            print("-----------YOUR BILL-------------\n")
                            for i in price:
                                total += float(i)
                            for i in range(3):
                                for dots in ['.','..','...']:
                                    print(f'\rGenerating{dots}',end = '',flush = True)
                                    time.sleep(0.5)
                            print("\r" +"  "*30,end= "")
                            for i,j in zip(cart,price):
                                print(f'{i}  {j}')
                            print("\n****************************")
                            animated_total(total)  
                            print("******************************")  
                            break
                        else:
                            continue  
                else:
                    if choice.lower() in menu:
                        print(f'{choice} has been added ✅ of ₹{menu[choice]}\n')
                        cart.append(choice)
                        price.append(menu[choice])
                    else:
                        print("the item you entered previously is not added to cart do you spell mistake ❌❌❌\n ")                   
        elif take.lower() == 'exit' or take == '3':
            break
            
        else:
            print("entered the wrong option")  
concessions()


