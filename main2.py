def maior(x,y,z):
    if x>y and x>z: 
        return f"o primeiro numero {x} é maior"
    elif y>x and y>z:
        return f"o segundo numero {y} é maior"
    elif z>x and z>y:
        return f"o terceiro numero {z} é maior"

for i in range(3):
    numero = int(input("digite um numero:"))
print(maior(i))



    