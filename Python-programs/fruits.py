fruits =[]

n = int(input("Enter how many fruits?:"))

for i in range(n):
    name= input("Enter the fruit name :")
    fruits.append(name)
    
for i in range (len(fruits)):
   print(i+1, ".", fruits[i])
   