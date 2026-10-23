print("----------Pizza order program-------------")
print("          ----Menu card----       ")

print("small_pizza = 100RS\nmedium_pizza = 200RS\nlarge_pizza = 300RS\npepporani_for_small_pizza = 30RS\npepporani_for_medium_or_large_pizza = 50RS\nextra_cheese_anySize_pizza = 20RS")

pizza = input("enter which size pizza you want - small, medium or large pizza : ")
pepporani = input("You want Pepporani :")
Cheese = input("You want more Cheese :")

if pizza == "small":
    if pepporani == "yes":
        if Cheese == "yes":
            Total = small_pizza + pepporani_for_small_pizza + extra_cheese_anySize_pizza
            print(f"Your order : \n Small pizza \n Pepporani \n Cheese \n Bill :{Total} RS")
        else:
            Total = small_pizza + pepporani_for_small_pizza
            print(f"Your order : \n Small pizza \n Pepporani \n Bill :{Total} RS")
    else:
        print("Your order : \n Small pizza \n Total prize 100 RS.")
        
if pizza == "medium":
    if pepporani == "yes":
        if Cheese == "yes":
            Total = medium_pizza + pepporani_for_medium_or_large_pizza + extra_cheese_anySize_pizza
            print(f"Your order : \n Medium pizza \n Pepporani \n Cheese \n Bill :{Total} RS")
        else:
            Total = medium_pizza + pepporani_for_medium_or_large_pizza
            print(f"Your order : \n Medium pizza \n Pepporani \n Bill :{Total} RS")
    else:
        print("Your order : \n Medium pizza \n Total prize 200 RS.")
    
if pizza == "large":
    if pepporani == "yes":
        if Cheese == "yes":
            Total = large_pizza + pepporani_for_medium_or_large_pizza + extra_cheese_anySize_pizza
            print(f"Your order : \n Large pizza \n Pepporani \n Cheese \n Bill :{Total} RS")
        else:
            Total = large_pizza + pepporani_for_medium_or_large_pizza
            print(f"Your order : \n Large pizza \n Pepporani \n Bill :{Total} RS")
    else:
        print("Your order : \n Large pizza \n Total prize 300 RS.")
        
        
print("Your order placed successfully!")
print("Bye!")

