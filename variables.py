def main():
    # ---------------------------------Variables name are key sensitive
    # String
    name = 'python'
    # int
    age = 30
    # List
    listOfThings = ['ball', 'car', 'plane']
    

    # ------------------------------Get the python keywords
    # import keyword
    # kw_List = keyword.kwlist
    #
    # for i in kw_List:
    #     print(i)

    # --------------------------------------Types
    # int, float, double

    # -------------------------------------------finding of min/max values
    # minValue = min(-1,5,-456,4,7846)
    # maxValue = max(-1,5,-456,4,7846)
    # print(maxValue, minValue)

    # -------------------------------------------String methods
    my_string = "Python is awesome"
    my_string = my_string.lower()
    my_string = my_string.split(" ")
    my_string = "-".join(my_string)
    print(my_string)

    """this is how to use f-strings"""
    # print(f"Person name is: {name} and age {age}")

    """this is how to iterate using [indexes]"""
    # print(len(my_string))
    #
    # print(my_string[-1])
    # #is the same as
    # print(my_string[len(my_string)-1])

    # print(my_string[0:6])
    test_number = '1234567894844343543843543843548435'
    # print(test_number[::2])  # -----------------------this is how to slice the string using defined step
    # # this is how to iterate a string backwards
    # print(test_number[::-1])
    # 'qwerty'[::-1]

    # # -------------------------------------this is how to iterate a number backwards (parse a number to a string using str() function)
    # num = 51543543453
    # u = str(num)
    # print(u[::-1])
    #
    # for i in reversed(test_number):
    #     print(i)

    # -----------------------------------------------------input function
    """all the input type values are treated as strings"""
    name1 = input('Введите имя: ')
    print(name1)
    """to convert input directly to int use int() function"""
    age1 = int(input('Введите возраст: '))
    print(type(age1))

    # ---------------------------------------------------import mudule example
    # print(f'variables module name is: {__name__}')
    """in case that we define name == main we can control modules importing --> if we run this module in main or any other file it will not be executed cuz there name is not equal with main"""
if __name__ == '__main__':
    print(f'this is the message if name == main: ', __name__)
    main()
else:
    print(f'sorry dude, name is not main')