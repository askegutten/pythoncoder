# oppgave 1

print("hello world")

# oppgave 2
print("what is your name?")
name =str(input())
print("hello",name)

# oppgave 3

number =int(input())
print(number*2)

# oppgave 4

print("what is your name?")
name = str(input())
print("what year are you born in?")
borny = int(input())
print("hello",name,"you are",2018-borny)

# oppgave 5
print("what is the year you were born in?")
borny =int(input())
b= 2018-borny

if b>=18:
	print("you can get your licens")
else:
	print("you can get a licens in",18-b,"years")

# oppgave 6

print("pick a number betwen 1 and 20")
number =int(input())
if number - 5 ==0:
	print("yay the number 5 is correct")
else:
	print("sorry the number",number,"is not correct")

# oppgave 7

print("i can add to numbers upp give me a number")
t1 =int(input())
print("give me a nother number")
t2 =int(input())
print(t1+t2)

# oppgave 8

print("i can do math give me a number an what you want to youse +-*/")
number = float(input())
print("give me a nother number")
number2 = float(input())
print("+-/*")
sign = str(input())
if sign == "-":
	print(number-number2)
elif sign == "/":
	print(number/number2)
elif sign == "+":
	print(number+number2)
else sign == "*":
	print(number*number2)

# oppgave 9

print("i can check if a number is a odd or even number")
number = int(input())
if number%2==1:
	print(number,"that is a odd number")
else:
	print(number,"that is a even number")

# oppgave 10
print("i can check if to name are the same give me a name")
name str(input())
print("give me a nother name")
name2 str(input())

if name == name2:
	print("the name",name,"and the name",name2,"are the same name")
else:
	print("the name",name,"and the name",name2,"are not the same name")

# oppgave 11
