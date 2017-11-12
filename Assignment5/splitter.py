import random

dataset = open('data/users.json', 'rb')
training = open('data/training.json', 'wb')
testing = open('data/testing.json', 'wb')

for line in dataset:
    r = random.random()
    if r < 0.8:
        training.write(line)
    else:
        testing.write(line)
        
dataset.close()
training.close()
testing.close()

