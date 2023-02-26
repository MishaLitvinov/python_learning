import random
number = random.randint(1, 100)
while True:
	print('Вгадай число між 1 і 100')
	reply = input()
	i = int(reply)
	if i == number:
		print('You win!')
		break
	elif i < number:
		print('More!')
	elif i > number:
		print('Less!')
