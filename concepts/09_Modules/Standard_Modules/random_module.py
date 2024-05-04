import random

num1 = random.random()
print("Random number:", num1) 
#fraction or decimal or any


num2 = random.randint(1, 10)
print("Random integer:", num2) 
#random integer number between range i.e 1 and 10

num3 = random.uniform(1.0, 10.0)
print("Random floating-point number:", num3) 
#random floating number between range i.e 1 and 10

seq1 = ["apple", "banana", "orange"]
item = random.choice(seq1)
print("Random choice:", item)
#random choice from these
seq2 = [1, 2, 3, 4, 5]
random.shuffle(seq2)
print("Shuffled sequence:", seq2)
#Shuffle sequence in reandom order

population = range(1, 11)
sample = random.sample(population, 3)
print("Random sample:", sample)
#any three random number from 11 number

random.seed(42)
num = random.random()
print("Random number with seed 42:", num)
