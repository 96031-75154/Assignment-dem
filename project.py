Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 'hello'
'hello'
>>> from random import randint
>>> print(randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9))
0 0 5 3 7 4
>>> print(randint(1,9),randint(2,8),randint(2,7),randint(3,6),randint(5,9),randint(0,9))
2 5 6 6 8 4
>>> 
>>> for i in range(6):
	print(randint(0,9),end=' ')

	
1 6 5 1 3 2 
>>> for i in range(6):
	print(randint(0,9),end=' ')

	
6 2 6 9 1 9 
>>> for i in range(6):
	print(randint(0,9),end=' ')

	
9 8 2 9 4 0 
>>> 
>>> otp = ' '
>>> for i in range(6):
	otp += str(randint(0,9))
	print(otp)

	
 0
 08
 089
 0894
 08947
 089471
>>> for i in range(6):
	otp += str(randint(0,9))
	print(otp)

	
 0894719
 08947197
 089471973
 0894719732
 08947197323
 089471973234
>>> 
>>> 