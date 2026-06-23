Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
# Non primitive datatypes ---- list --- set --- tuple --- dictionary

# List
#------

Office = ['Excel','Teams','Outlook','MS Access']

office
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    office
NameError: name 'office' is not defined. Did you mean: 'Office'?
Office
['Excel', 'Teams', 'Outlook', 'MS Access']

Office[2]
'Outlook'
Office[2]='Co pilot'

Office
['Excel', 'Teams', 'Co pilot', 'MS Access']
Office[2:]
['Co pilot', 'MS Access']
Office[:,2,-1]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    Office[:,2,-1]
TypeError: list indices must be integers or slices, not tuple
TypeError: list indices must be integers or slices, not tuple
SyntaxError: invalid syntax






Office[:,-2,-1]
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    Office[:,-2,-1]
TypeError: list indices must be integers or slices, not tuple



>>> 
>>> Office.append('Test1')
>>> Office
['Excel', 'Teams', 'Co pilot', 'MS Access', 'Test1']
>>> Office.extend('Test2','Test3')
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    Office.extend('Test2','Test3')
TypeError: list.extend() takes exactly one argument (2 given)
>>> Office.extend(['Test2','Test3'])
>>> Office
['Excel', 'Teams', 'Co pilot', 'MS Access', 'Test1', 'Test2', 'Test3']
>>> 
>>> Office.index('Test1')
4
>>> Office.insert(4,'Test5')
>>> Office
['Excel', 'Teams', 'Co pilot', 'MS Access', 'Test5', 'Test1', 'Test2', 'Test3']
>>> Office.pop()
'Test3'
>>> Office
['Excel', 'Teams', 'Co pilot', 'MS Access', 'Test5', 'Test1', 'Test2']
>>> Office.pop(4)
'Test5'
>>> Office
['Excel', 'Teams', 'Co pilot', 'MS Access', 'Test1', 'Test2']
>>> Office.remove('Test2')
>>> Office
['Excel', 'Teams', 'Co pilot', 'MS Access', 'Test1']
