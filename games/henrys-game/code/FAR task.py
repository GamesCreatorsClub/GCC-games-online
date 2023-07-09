import random
keywords = ["variable","constant","sequence","selection","elif","integer","float"]
questions = ["a datatype that has a set value / text belonging to itself that can vary","something that is always happening","something happening in order","choosing something","an if statement / line of code which executes different code depending on a chosen input","a datatype for storing numerical units","a datatype for dividing, etc"]
while True:
    num = random.randint(1,7)
    num = num - 1
    num1 = random.randint(0,6)
    num2 = random.randint(0,6)
    num3 = random.randint(0,6)
    numR = random.randint(1,3)
    if numR == 1:
        num1 = num
    if numR == 2:
        num2 = num
    if numR == 3:
        num3 = num

    question = input("Is a ",keywords[num],":\nA: ",questions[num1],"\nB: ",questions[num2],"\nC: ",questions[num3])
    if question == question[num]:
        print("well done bro")

