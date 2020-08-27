'''
Review Python ICE
MSIS 5193
Completed Aug 26, 2020
'''
#-------------------------#
hometown = "Klang" #town of high school graduated
x = 298784 # given value from ice

#2 codes function for j & l sum
j, l = 5, 10
print(j+l)

z = j+l #value of j & l sum

t, q, r, s = 'education' #assign value to 4 vars

#identify data types
x = ["apple", "banana", "cherry"]
y = ("apple", "banana", "cherry")
f = False
g = 'covid-19'
print(type(x),type(y),type(f),type(g))

# if-else and scope
x = 0
j = 3

def funky(arg1, arg2):
	global x, j # global keyword
	x = 1
	j = 5
	if arg1 > arg2:
		print('arg1 is greater than arg2')
	else:
		print('arg1 is not greater than arg2')
	print(j)
funky(x, j)
print(x)
print(j)


# Iteration
lunches = ['burger','apple','soba','chahan']
# 2 codes for-loop
for i in lunches:
	print(i)

#break when is apple
for i in lunches:
	print(i)
	if i == 'apple': 
		print("Break Loop!")
		break