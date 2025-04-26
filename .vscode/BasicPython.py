print("Ankita")

a=10
b=5
c=a+b
print(c)


s="Ankita"
print(type(s))

print(1+2)

print(6*4)

A=10
print(A)


a=20
print(a)

print(A)
print(a)

a=30
a=40
a=50
print(a)
# it takes latest value

a=10
b=10
print(id(a))
print(id(b))


d=3.4
print(type(d))

c=5+8j
print(type(c))

print(c.real)
print(c.imag)


a,b,c=12,34,56
print(b)
b=78
print(a,b,c)


'''Hi all
good afternoon
today march 1st but not thursday'''


'''Hi all
good afternoon
today march 1st but not thursday'''
a=10
print(a)


#Numerical operation
a=10
b=5
print(a+b)
print(a-b)
print(a/b)
print(a*b)
print(a//b) #floor division
print(a%b)
print(a**b)


a="Ankita"
print(a[::-1])

print(len(a))

print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5])

a="Ankita"
print(a[0:3])
print(a[0:])
print(a[::])
print(a[::-1]) #Reverse
print(a[::2])
print(a[0:3000])

'''a="Akshay"
a="ankitha"
a[0]="S"
a'''

#Strings are immutable we cant change particular value of a string 


#2notebook

print("Good Afternoon")

a=10
b=20
c=a+b
print(c)

a=10
b=20
c=a+b
print("Addition=",c)

a=10
b=20
c=a+b
print("Addition of a=",a,"and b=",b,"is c=",c)

a=10
b=20
c=a+b
print("Additional of a={0}, and b={1}, and c={2}".format(a,b,c))

myvar="Ankita"
print(myvar)

a=b=c=d="orange"
print(a)

a="python"
b="is"
c="awesome"
print(a+b+c)

#type casting
a='5'
b="ankita"
print(a+b)

print(int(35.67))

a="Ankita"
print(len(a))

x="Welcome"
print(x[3])

a="The Best book in the world is written by JK Rowling"
print("Book" not in a)

a="ankita"
print(a.upper())

a="ANKITA"
print(a.lower())

#to remove unwanted Spaces at begining and Ending is Strip 
a="         a n  k  i  t  a       "
print(a.strip())

#Replace function
a="Ankita"
print(a.replace("a","Z"))

a="Ankta&Ashokrao&Kharpade"
print(a.split("&"))

#Anagram? #An anagram is when we rearrange the letters of one word to form another word.
from collections import Counter
a="AnkitaAshokraoKharpade"
b=Counter(a)
print(b)

from collections import Counter
a=input("Enter the name apart from charan any name is okay")
b=Counter(a)
print(b)

#Swapcase=reverse what ever in caps to small and Viceversia
a="AshoKraoKharPade"
b=a.swapcase()
print(b)

# Input values
a = 3
b = 2
c = 9

# Display output
print(f"a={a} b={b} c={c}\n\neg 2 a=2 b=2 c=4")

#in oneline code
print("a=3 b=2 c=9\n\neg a=2 b=2 c=4")

#anotherEx
print("a=4 b=5 c=10\n\neg a=10 b=20 c=40")

# Comparision Operators
a=5
b=10
print(a==b)
print(a!=b)
print(a>b)
print(a>=b)
print(a<b)
print(a<=b)

#Boolean values
#true and False
print(10<=10)

#Conditionals

x=5
if x<5:
    print("Hai Bro")
else:
    print("Bye Bro")

X=5 
print("hai Bro") if x<5 else print("Bye Bro")

a=300
b=200
if b>a:
    pass
else:
    print("fail")

#Conditional Statements 
#conditionals statement are if elif else
#conditionals statement is control the flow of a program based on conditions
#If statement: the basic conditional statement that determines if a block of code should be executed
#If-else statement:Controls the flow of execution based on a condition.
#If-elif-else statement:Evaluates multiple cindition sequentially and executes different blocks of code.
#Nested if statement:Checks for a secondary condition if the first condition executes as true.

'''if statement: true

    if statement2 : true
    
         if statement3 : true
         else3:
         statement3 will be print
    
    else2:
    statement2 is print
else: statement is print'''


mymoney=int(input())
price=int(input())
if price<=mymoney:
    print("I can able to buy")
else:
    print("I can't buy")

a=500
shirt_price=200
pant_price=500
coat_price=800
my_size='L'
size_Store=['M','L','S','XS','XXL']
my_Fav_Color='Black'
store_clr=["Whte",'red','Black','Orange']
if coat_price <=a:
    print("I will buy a coat")
elif pant_price<a:
    print("I will buy a pant")
elif shirt_price<a:
    print("I will buy a shirt")
    if my_size in size_Store:
        print("I can continue my shoppping")
        if my_Fav_Color in store_clr:
            print("I will choose my fav")
        else:
            print("Bye I am not going to Buy in this")
    else:
        print("My size is not available")
else:
    print("I won't buy")
    
course=['DSM','DSA','JAVA',"python"]
price=30000
mentor="charan"
if "python" in course and price<=40000 and "charan"==mentor:
    print("I will buy")

user_name="charan"
password="omsairam"
if user_name==input("Enter your username") and password==input("Enter your password"):
    print("You have logged in Successfully")
else:
    print("Enter correct name and password")

mobile_no=9848022338
otp=9877
if mobile_no==int(input("Enter your mobile number")):
    print("You are registered user")
    if otp==int(input("Enter the otp sent to your Mobbile no")):
        print("You have logged in Successfully")
    else:
        print("incorrect OTP please Re enter Again correctly")
else:
    print("You are not a Registered user")

sum=10
def cal():
    sum=30
    sum=sum+20
    current_Sum=200
    totalsum=sum+current_Sum
    print(totalsum)
cal();
print(sum)

sum=10
def cal():
    global sum
    sum=sum+20
    current_Sum=200
    totalsum=sum+current_Sum
    print(totalsum)
cal();
print(sum)

mobile_no={9848022338,9888888888,8464808080}
otp=9877
if int(input("Enter your mobile no")) in mobile_no:
    print("You are registered user")
    if otp==int(input("Enter the otp sent to your Mobbile no")):
        print("You have logged in Successfully")
    else:
        print("incorrect OTP please Re enter Again correctly")
else:
    print("You are not a Registered user")


#Reverse of A string
a="python"[::-1]
print(a)

sum=10
def cal():
    #global sum
    sum=sum+20
    current_Sum=200
    totalsum=sum+current_Sum
    print(totalsum)
cal();
print(sum)

num = int(input("Enter a number"))
if num>0:
    print("the number is",num)
    if num%2==0:
        print(f"Entered Number {num} is an even number")
    else:
        print("Entered number is {num} is odd number")
else:
    print("Entered number is not a number")

 sum=10
def cal():
    global sum
    sum=sum+20
    current_Sum=200
    totalsum=sum+current_Sum
    print(totalsum)
cal();
print(sum)

a = ["Python","Java","C++"]
a.reverse()
print(a)

d = "Ankita"[::-1]
print(d)

s={1,2,3,4,5}
for i in s:
    print(i)

t=(12,3,4,45,"Sudha","Charan")
t_int=[]
t_str=[]
for i in t:
    if type(i)==str:
        t_str.append(i)
    elif type(i)==int:
        t_int.append(i)

t_int
t_str
















