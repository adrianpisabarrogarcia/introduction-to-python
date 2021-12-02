import random
array_of_ip_address = []

for i in range(0, 10):
    ip_address = str(random.randint(0, 255))+"."+str(random.randint(0, 255))+"."+str(random.randint(0, 255))+"."+str(random.randint(0, 255))
    array_of_ip_address.append(ip_address)

print("\n")
print("La lista de IPs ingresadas es: {}".format(array_of_ip_address))
print("\n")
