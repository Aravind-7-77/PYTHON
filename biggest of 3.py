Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=10
>>> b=54
>>> if(a>b):
...     print('a is big')
... else:
...     print('b is big')
... 
...     
b is big
>>> 
>>> a=23
>>> b=65
>>> c=21
>>> if(a>b and a>c):
...     if(b>c):
...         print(a,b,c)
...     else:
...         print(a,c,b)
... elif(b>a and b>c):
...     if(a>c):
...         print(b,a,c)
...     else:
...         print(b,c,a)
... else:
...     if(a>b):
...         print(c,a,b)
...     else:
...         print(c,b,a)
... 
...         
65 23 21
>>> 
>>> 
>>> a=int(input("enter value")
...  b=int(input("enter value")
...        
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> a=int(input("enter value"))
...  b=int(input("enter value"))
...        
SyntaxError: multiple statements found while compiling a single statement
