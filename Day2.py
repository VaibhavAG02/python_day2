user_value=int(input('Enter a number\n'))
if user_value>=1:
    if user_value<=60:
        if user_value<=20:
            a=user_value
            b=0
            c=0
            print("a=",a)
            print("b=",b)
            print("c=",c)
        elif user_value>20:
            if user_value<=30:
                a=20
                b=user_value-20
                c=0
                print("a=",a)
                print("b=",b)
                print("c=",c)
            else:
                a=20
                b=10
                c=user_value-30
                print("a=",a)
                print("b=",b)
                print("c=",c)
    else:
        print("Value must be less than or equal to 60")
else:
    print("Value must be greater than or equal to 1")