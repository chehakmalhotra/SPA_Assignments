import random
import matplotlib.pyplot as plt
coin_tosses=20
p=0.8
q=1-p

#plot a graph between number of heads per trial

num_heads_per_trial_p1 = []

for i in range(1000):
    number_of_heads=0
    

    for i in range(coin_tosses):
        if random.random() < p:
            number_of_heads=number_of_heads+ 1

    num_heads_per_trial_p1.append(number_of_heads)



new_p=0.5

#plot a graph between number of heads per trial

num_heads_per_trial_p2 = []

for i in range(1000):
    number_of_heads=0
    

    for i in range(coin_tosses):
        if random.random() < new_p:
            number_of_heads=number_of_heads+ 1

    num_heads_per_trial_p2.append(number_of_heads)


plt.subplot(1, 2, 1)
plt.hist(num_heads_per_trial_p1)
plt.xlabel('Number of Heads')
plt.ylabel('Frequency')
plt.title('Histogram for p=0.8')

# Plot for p=0.5
plt.subplot(1, 2, 2)
plt.hist(num_heads_per_trial_p2)
plt.xlabel('Number of Heads')
plt.ylabel('Frequency')
plt.title('Histogram for p=0.5')


plt.show()