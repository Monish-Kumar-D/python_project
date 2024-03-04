import re
import cowsay
import sys
import math
import csv
import tabulate
import inflect
import pyfiglet
from datetime import date,datetime
#AIM is to make the grocery store
p=inflect.engine()



def main():
    print(cowsay.milk('Welcome to H&M Store'))
    print('H&M offers fruits, vegetables, households and schoolsupplies')
    print()
    while True:
           name=input("Enter your name here: ")
           if re.search("^[a-zA-Z]+$",name):
                        break
           else:
               print("Enter a valid name")
    dict1={}
    responce="y"
    repetions,order_repetions=0,0
    while responce=="y":
       category=input(f'Which category you\'re looking for today {name}? ').strip().lower()
       print()
       if validate(category):
          avail_products(category)
       elif repetions>2:
           sys.exit("Too many tries,try after sometime")
       else:
           print('Oops!! enter a valid category')
           repetions+=1
           print()
           continue
       products_dict1=dict_creater(category)
       product_list=grocery_list(products_dict1,dict1)
       responce=input(f"Do you want to continue shopping on other categories ?(Y/N)").lower().strip()
    print(f"Biller name:{name}")
    print()
    for i,j in product_list.items():
        print(i,':','$',j)
        print()
    costlist=list(product_list.values())
    total_cost=calculation(costlist)
    print("The total cost of your purchase is :$",total_cost)
    print()
    command=input("Do you have any coupon ").lower()
    if command in ["y","yes"]:
         code=input('enter any coupons that you have: ')
         final=coupon_codes(code,total_cost)
         if final == total_cost:
             print(f'it is not a valid coupon\n${total_cost} is the final cost')
             print()
             print('in words ',p.number_to_words(total_cost),'dollars')
             print()
             input_money(float(total_cost))
         else:
             print(f"{name}!! Your coupon is applicable \n${final} is the final cost")
             print()
             print('in words:',p.number_to_words(final),'dollars')
             print()
             input_money(float(final))
    else:
        print(f"{name}!! you need to pay \n${total_cost}")
        print('in words:',p.number_to_words(total_cost),'dollars')
        input_money(float(total_cost))
    feedback(name)




#inputs that are need to be installed
# diplaying the csv file in a table


def validate(promt):
    list1=['fruits','vegetables','households','schoolsupplies']
    if promt.lower().strip() in list1:
        return True
    else:
        return False



def avail_products(category):
    list2=[]
    with open(category+'.csv') as file1:
        list1=csv.reader(file1)
        for line in list1:
            list2.append(line)
        print("Here the list of products currently available in the store ")
        print()
        print(tabulate.tabulate(list2[1:],headers=list2[0],tablefmt='fancy_grid'))
        print()




#gives the dictionary of products and prices in the given category
def dict_creater(category):
    with open(category+'.csv') as file2:
        lines=csv.DictReader(file2)
        dict1={}
        for line in lines:
            product,prices=line['products'],line['prices']
            dict1[f'{product}'] = prices
        return dict1



#creat a custamised list of products for the user
def grocery_list(dictionary,dict1,order_repetions=0):
        order=input("which one of these you wanna buy? ").strip().lower()
        print()
        if order in list(dictionary.keys()):
            while True:
                try:
                    numbers =int(input(f"how many {order} you want to buy? "))
                    break
                except ValueError:
                    print("Enter a valid integer ")

            print()
            cost=numbers*float(dictionary[order][1:])
            dict1[order]=format(cost,".2f")
            responce=input('Do you want to purchase more?(Y/N) ').lower().strip()
            print()
            if responce == 'y':
                grocery_list(dictionary,dict1,order_repetions)
            else:
                return dict1

        elif order_repetions>1:
            sys.exit("Too many unsuccessful tries")

        else:
            print('the product youre looking for is not available')
            print()
            order_repetions+=1
            grocery_list(dictionary,dict1,order_repetions)
        return dict1



#money and calculation
def calculation(list1):
    sum=0
    for i in list1:
        sum+=float(i)
    if sum>10:
        print("Since we have standard discount of 10% for the coustomers \nwho ordered more than $10 \nyours $",sum)
        print()
        total=sum-sum*0.10
        return format(total,".2f")
    else:
        return format(sum,".2f")



#ask them to use coupon codes
def coupon_codes(code,initial_cost):
    with open("coupon.txt","r") as codes:
        coupon_codes_list=codes.readlines()
        list1=[]
        for i in coupon_codes_list:
            list1.append(i[0:4])
        if code in list1:
             cost=float(initial_cost) - 0.15*float(initial_cost)
             return format(cost,".2f")
        else:
             return initial_cost



#take the money input from the user
def input_money(amount):
    print('Amount Due: $',amount)
    while float(amount)>0:
        while True:
           try:
                amount_deposited=float(input("Charges: "))
                break
           except ValueError:
               print("Enter a valid integer ")
        amount-=amount_deposited
        amount=float(format(amount,".2f"))
        if amount==0:
            print('Items purchased!!!')
            print()
        elif amount>0:
            print("Still need to pay:$",amount)
            print()
        else:
            print("seems you paid extra here is your $",amount*(-1))
            print()
            break



#ask the customer for the feedback and append that in another file
def feedback(name):
    with open("feedback.txt",'a') as fp:
        customer_feedback=input('Your feedback helps us to improve our interactive interfaces userfriendly \nEnter your feedback here: ')
        now=datetime.now()
        today_date=date.today()
        current_date=today_date.strftime(" %d/%m/%Y ")
        curent_time=now.strftime(" %H:%M:%S ")
        fp.write(current_date)
        fp.write(curent_time)
        fp.write(f"customer name:{name} feedback: ")
        fp.write(customer_feedback)
        fp.write("\n")
        print("Thank you,your responce will be respected")
        print()
        print("Thank You for your shopping with us!!!")
        print()
        sys.exit(pyfiglet.figlet_format(f"THANK YOU {name}",font='slant'))



if __name__=="__main__":
    main()
