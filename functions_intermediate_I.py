import random
def randInt(min= 0, max= 100):
    num = round(random.random() * 100)
    return num
# print(randInt()) # should print a random integer between 0 to 100


def randInt(min= 0, max= ""):
    num = round(random.random() * 50)
    return num
# print(randInt(max=50)) # should print a random integer between 0 to 50

def randInt(min= 50, max= 100):
    num = round(random.random() * (max - min) + 50)
    return num
# print(randInt(min=50)) # should print a random integer between 50 to 100
def randInt(min= 0, max= 500):
    num = round(random.random() * (max - min) + 50)
    return num
# print(randInt(min=50, max=500))
# should print a random integer between 50 and 500


# python functions_intermediate_I.py

# echo "# functions_intermediate_I" >> README.md
# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/jcambray10/functions_intermediate_I.git
# git push -u origin main