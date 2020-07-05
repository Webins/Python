def avg(*args): #convert every passed argument in a tuple
	sum = 0
	for n in args:
		sum += n
	return sum / len(args)

nums1 = [1,2,3,4,5,6,7,8,9,10]
nums2 = (10,20,30,40,50,60,70,80,90,100)

print(avg(*nums1)) #unpacking a list into individual items
print(avg(*nums2)) #unpacking a tuple into individual items


def display_ip_info(ip, gateway, public_ip):
	print(f"Ip:{ip}, Gateway:{gateway}, Public Ip:{public_ip}")
	
ip ={
"ip": "192.168.1.105",
"gateway": "192.168.1.1",
"public_ip": "221.54.78.30"
}

display_ip_info(**ip)
