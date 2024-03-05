# Best Buy, The Online Market Place
#### Video Demo:  [video link](https://youtu.be/zv9DKwvuMOA?si=dfqkBt7eXWa1bRJs)
#### Description: Best buy is a python program which is used to make a user-friendly digital adaptation of selling market of a popular shop "H&M"


## Introduction:
I am Monish Kumar from TamilNadu,India and this is my CS50P Final Project

This is a shopping market made with python alone.It allows the user to buy fruits,vegetables,household items and schoolsupplies.Since it is made only for the terminal window, libraries like cowsay,figlet and inflect been used to make the terminal user interactive

Attributes used to construct this programs includes:

## Files used
* A CSV file of fruits and its respective cost
* A CSV file of vegetables and its respective cost
* A CSV file of households and its respective cost
* A CSV file of schoolsupplies and its respective cost
* A text file for discount coupons
* A text file to indicate the libraries installed for this project developement
* A text file to store the feedback from the user about the user experience

## Libraries installed
* cowsay
* pyfiglet
* tabulate
* inflect

## Structure of the program

* This program starts by introducing the store name ** H&M ** and the available category of products.Then it uses its first interactive mode to ask the name of the user and the category that he/she wants to look for.The name is being checked by using a regular expression to obtain a valid name.If user accidentaly chosed and spelled wrong category,the program itself figures that out and promt the user again to enter category.if user failed to enter a valid category for multiple times,program automatically terminates with sys.exit saying the user "Too many tries,try after sometime"

* Using the above input for category, the csv file of that category been located and opened as input file and the contents of those available products in that particular CSV file been tabulated and displayed in the terminal for the user to know what are the currently available products

* Then after, the user been asked for the products that they want from the available products which is been displayed previously. Here too, if user failed to enter a valid product for multiple times,program automatically terminates with sys.exit saying the user "Too many unsuccessful tries"

* Then programs asks the how many of those chosen product that they want to buy which is later used to calculate the total amount that the user need to pay for that particular product.Here the number of products that they want is been checked using try and except, then the programs ask wheather the user need more products from the same category, if user agreed for that then the above step been repeated

* If the user chosed to leave the current category, the user been asked whether they are intrested to look into other category. If agreed, the user been reprompted to choose that category they are looking for and that category been tabulated and displayed same as the second step

* After they completed choosing the items that they want, the products that the user bought and and its respective pricing been displayed and the grand total displayed. If the user bought for more than a certain amount, it is applicable to the standard discount and the total after discount been displayed

* The user been asked for a coupon code that they might have so that extra discount been given to the user. After the program takes the input from the user, the coupon code been checked from already available text file of several coupon codes. If the user input matches any one of those coupons then it is applicable for discount and the total been reduced by subtracting the discount and displayed to the user

* Then user been asked to enter the money that they need to pay in order to purchase the products. If the user entered the exact amount then it moves to next step or else it repromts the user to enter the remaining amount that they need to pay. If they paid excess amount then the program returns the remaining amount to the user

* Finally after the purchace, the user been asked to write their feedback about the store and been seperately stored in a text file so that it will be useful for the store to improvise thier user experience

* Then program terminates with greeting the user for their purchace
# >>>End of the program<<< #
## Highlights
* Basic value assigns, type convertions
* The code uses basic interactive input functions
* Usage of conditional statements
* Loops(for/while) and also uses recursive functions
* format strings
* Calling functions and passing parameters to the function
* Handling several Data Structes such as Lists, Dictionaries etc...
* Basic I/O files handling
* Installation and usage of several libraries
* Unit Testing
# python_project
