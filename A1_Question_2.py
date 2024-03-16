import random
import matplotlib.pyplot as plt

import math

time=5
lambdaa=5

x_s = []
y_s=[]

for x in range(int(time * lambdaa)*2):
    x_s.append(x)

for x in range(int(time * lambdaa) *2):
    y_s.append((math.exp(-lambdaa * time)*(lambdaa * time) ** x) / math.factorial(x))
   


theoretical_mean = lambdaa * time

print('Theoretical Mean: ', theoretical_mean)

new_lambdaa=15

xn_s = []
yn_s=[]

for x in range(int(time * new_lambdaa)*2):
    xn_s.append(x)

for x in range(int(time * new_lambdaa)*2):
    yn_s.append((math.exp(-new_lambdaa * time)*(new_lambdaa * time) ** x) / math.factorial(x))

theoretical_mean = new_lambdaa * time

print('Theoretical Mean: ', theoretical_mean)

plt.figure(figsize=(12, 5))

plt.subplot(121)
plt.bar(x_s, y_s)
plt.xlabel('Number of Arrivals')
plt.ylabel('Probability Density')
plt.title('Density of Arrivals in Continuous Time Interval (0, 5)]')



plt.subplot(122)
plt.bar(xn_s, yn_s)
plt.xlabel('Number of Arrivals')
plt.ylabel('Probability Density')
plt.title('Density of Arrivals in Continuous Time Interval (0, 5)]')
plt.tight_layout()

plt.show()





x_s=[]
lambdaa = 5
for i in range(100):
    x_s.append(i*0.02)


y_s=[]

for t in x_s:
    pdf = lambdaa * math.exp(-lambdaa * t)
    y_s.append(pdf)


plt.plot(x_s, y_s)

plt.xlabel('Inter-Arrival Time (hours)')
plt.ylabel('Probability Density')



plt.show()




    





    
    

   
    
     


