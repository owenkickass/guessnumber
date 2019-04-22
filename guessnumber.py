import random
r = random.randint(1,100)
while True:
	num = input('please input a number')
	num = int(num)
	if r == num:
		print('your answer is correct')
		break
	else:
		if r > num:
			print('bigger')
		if r < num:
			print('smaller')
