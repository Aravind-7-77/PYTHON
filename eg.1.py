#write a program to display all prime numbers within an interval(2)
start=int(input("Enter the start of the interval"))
end=int(input("Enter the end of the interval"))
print("Prime number between",start,"and",end,"are.")
for num in range(start,end+1):
    if num>1:
        for i in range(2,num):
          if num%i==0:
              break
          else:
              print(num)


#Demonstrate the following operators in python with sutable examples(3)
#arithmetic operators
a=10
b=5
print("addition:",a+b)
print("subtraction:",a-b)
print("multiplication:",a*b)
print("division:",a/b)
print("modulus:",a%b)
print("exponention:",a**b)
print("floor division:",a//b)

          
#write a python program to print day name for a given for a given day number(4)
def get_day_name(day_number):
    days=["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]
    if 1<=day_number<=7:
        return days[day_number-1]
    else:
        return("Invalid day number please enter a number between 1 and 7")
day_num=int(input("enter a day number(1-7): "))
print("Day:",get_day_name(day_num))


v#write a program to check if a num is even or odd(5)
num=int(input("Enter a number:"))
if num%2==0:
    print("number is even")
else:
    print("number is odd")


#write a program to create tuples(name,age,address,college)for atleast two members,concatinate the tuples,and print the concate(6)
#creating tuples for two numbers
member1=("alice",22,"123 maple st","abc university")
member2=("bob",23,"456 oak ave","xyz college")
#concatenating the tuples
concatenated_tuple=member1+member2
#printing the concatenated tuple
print("concatenated tuple:",concatenated_tuple)
