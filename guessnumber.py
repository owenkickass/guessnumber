import random
r = random.randint(1,100)
count = 0
while True:
	count = count + 1
	num = input('please input a number')
	num = int(num)
	if r == num:
		print('your answer is correct')
		print('this is your', count ,'time')
		break
	elif r > num:
		print('bigger')
	elif r < num:
		print('smaller')
	print('you already tried',count, 'times')
