try:
    print(x)
except:
    print("there is an error")


try:
    # x=2
    print(x)
except:
    print("There is an error")
else:
    print("There is no error")
finally:
    print("succesfully completed")

# try:
#     print(x)
# except NameError:
#     print("variable not defined")
# except:
#     print("error")

# a=int(input("Enter a positive number"))
# if a<0:
#     raise Exception("negative number not allowed")
# else:
#     print(a)

# x="dev"
# if type(x)==str:
#     raise Exception("string is not allowed")
# else:
#     print(x)

# try:
#    a=int(input("Enter the 1st number"))
#    b=int(input("Enter the 2nd number"))
#    c=a/b
# except ValueError:
#    print("integer value is only allowed")
# except ZeroDivisionError:
#    print("zero is not allowed")
# except:
#    print("error is occured")
# else:
#    print(c)
   
