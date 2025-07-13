import time
import sys
def shopping_cart():
    food= []
    price = []
    total = 0
    while True:
        choice = input("name of food item \n(Or Enter x exit)  => ")
        if choice.lower() == 'x':
            if food == []:
                print("Your cart is empty")
            else:    
                print("......your cart is ready.......\n")
                for i in range(2):
                    for dots in [".", "..", "..."]:
                        print(f"\rGenerating{dots}   ", end="", flush=True)
                        time.sleep(0.5)
                print("\r"+""*10 ,end='')        
                for i,j in zip(food,price):
                    print(f"{i} = ${j} ")
                    time.sleep(0.5)
                    total += j
                time.sleep(0.5)    
                print('.........................................')
                print(f"<<<< You have to pay this amount ${total} >>>>")
                print("...........................................")
                break
            break
        else:
            food.append(choice)
            while True:
                pricex = input(f"Enter the price of {choice} => ")
                try:
                    pricex =float(pricex)
                    price.append(pricex)
                    break
                except:
                    print("Invalid price enter the number")    

shopping_cart()

                    
