def avg(*args): #convert every passed argument in a tuple
	sum = 0
	for n in args:
		sum += n
	return sum / len(args)


print(avg(10.5,454,57.8878,4.5,45,54,47787,87845,1451,545,454,5,58.45,4545))	

def ensure_correct_info(*args):
	if "Colt" in args and "Steele" in args:
		return "Welcome back Colt"
	return "Not sure who you are"
	
print(ensure_correct_info())

print(ensure_correct_info(1, True, "Steele", "Colt"))
