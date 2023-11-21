import random

comp = random.randint(0,2)
# print(comp)
print(".............Snake Gun Water Game...............")
user = int(input("Enter 0 for snake, 1 for water and 2 for gun: "))

def test(comp, user):
    if (comp == user):
        return 0
    if (comp == 0 and user == 1):
        return -1
    if (comp == 1 and user == 2):
        return -1
    if (comp == 2 and user == 0):
        return-1
    return 1

score = test(comp, user)

print("You: ", user)
print("Computer: ", comp)

if(score == 0):
  print("Its a draw")
elif (score == -1):
  print("You Lose")
else:
  print("You Won")

