Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
# Python String handling
#-------------------------

# String Concadenation
# String Concatenation

'Elango' + '35'
'Elango35'

'Elango' + 'Dhamodharan'
'ElangoDhamodharan'

'Elango' + str(35)
'Elango35'

# String repetition
#------------------

Name='Elango'

Name * 5
'ElangoElangoElangoElangoElango'
# String Formating
#---------------------

Age = 35

print('Name is {0} and age is {1})
      
SyntaxError: unterminated string literal (detected at line 1)
print('Name is {0} and age is {1}')
      
Name is {0} and age is {1}
Name is {0} and age is {1}
      
False


print('Name is {0} and age is {1}'.format(name,age))
      
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    print('Name is {0} and age is {1}'.format(name,age))
NameError: name 'name' is not defined. Did you mean: 'Name'?
print('Name is {0} and age is {1}'.format(name,Age))
      
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    print('Name is {0} and age is {1}'.format(name,Age))
NameError: name 'name' is not defined. Did you mean: 'Name'?
print('Name is {0} and age is {1}'.format(Name,Age))
      
Name is Elango and age is 35
Name is Elango and age is 35
      
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    Name is Elango and age is 35
NameError: name 'Elango' is not defined

# Automated formating
      
print('Name is %s and age is %d' %(Name,Age))
      
Name is Elango and age is 35
print('Name is %s and age is %s' %(Name,Age))
      
Name is Elango and age is 35
Name is Elango and age is 35
      
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    Name is Elango and age is 35
NameError: name 'Elango' is not defined
>>> 
>>> # General formatting
...       
>>> #----------------------------
...       
>>> name = 'Nakshathra'
...       
>>> age = 6
...       
>>> city = 'Chennai'
...       
>>> print('My baby name is',name,'age is' age,'hometown'city)
...       
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print('My baby name is', name , 'age is' age,'hometown', city)
...       
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print('My baby name is',name,'age is',age,'hometown',city)
...       
My baby name is Nakshathra age is 6 hometown Chennai
