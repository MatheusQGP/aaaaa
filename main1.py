def maior_dos_dois(x,y):
    if x>y:
        return f"o{x} é maior que o {y}"
    elif y > x:
        return f"o{y}é maior que o {x}"
    else:
        return f"o os numeros sao iguais "

print(maior_dos_dois(5,8))