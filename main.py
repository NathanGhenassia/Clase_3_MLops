#Codigo para la suma de dos numeros
def suma(num1: int, num2: int) -> int:
    return num1 + num2


if __name__ == '__main__':
    print(suma(num1=2, num2=4))



#Codigo para la resta de dos numeros
def resta(num1: int, num2: int) -> int:
    return num1 - num2


if __name__ == '__main__':
    print(resta(num1=2, num2=5))



#Reconocimieto de gatos y perros

def gato(animal: str):
    if animal == 'cat':
        return True
    else:
        return False

if __name__ =='__main__':
        print(gato(animal = "cat"))