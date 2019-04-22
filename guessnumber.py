import random
r = random.randint(1,100)
while True:
	num = input('please input a number')
	num = int(num)
	if r == num:
		print('your answer is correct')
		break
	elif r > num:
		print('bigger')
	elif r < num:
		print('smaller')
		