from datetime import date

print("Bienvenido al programa")
parsec = input("Introduzca los parsec:")

lightyears = (3.26156 * int(parsec))

print(str(parsec) + " parsec, is " + str(lightyears) + " lightyears")

date.today()
print("Today's date is: " + str(date.today()))


#print("Calculadora")
#first_number = input("Primer número: ")
#second_number = input("Segundo número: ")
#print(int(first_number) + int(second_number))