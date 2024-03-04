from project import validate,dict_creater,calculation,coupon_codes

def main():
    test_validate()
    test_dict_creater()


def test_validate():
    assert validate("fruits") == True
    assert validate("Fruits") == True
    assert validate("hello") == False



def test_dict_creater():
    assert dict_creater("fruits")=={
"apples":"$1.44",
"bananas":"$0.32",
"blueberries":"$4.19",
"peaches":"$2.03",
"avocados":"$1.09",
"oranges":"$0.95",
"strawberries":"$5.29",
"cantaloupe":"$2.98",
"pears":"$0.80",
"grapes":"$3.48"}

    assert dict_creater("schoolsupplies")=={"mechanicalpencils":"$3.97",
"notebook":"$1.48",
"indexcards":"$6.99",
"pencilsharpener":"$8.99",
"filefolders":"$13.99",
"stapler":"$9.75",
"ballpointpens":"$1.27"}

def test_calculation():
    assert calculation([1,3,2,4])=='10.00'
    assert calculation([4,3,7])=='12.60'


def test_coupon_codes():
    assert coupon_codes('SH04','10.00')=='8.50'
    assert coupon_codes('AB06','10.00')=='10.00'

if __name__=="__main__":
    main()
