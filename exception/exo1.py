import sys
#EXERCIE 1 
def divEntier(x: int, y: int) -> int:
    if x < 0:
        raise ValueError ("x doit être positif") 
    if y <= 0:
        raise  ValueError ("y doit être positif et supérieur à 0")
    if x < y:
        return 0
    else:
        x = x - y
    return divEntier(x, y) + 1

def main():
    try:
        x= int(input('nombre entier: '))
        y= int(input('nombre entier: '))
    except ValueError:
        print ("Entrez un entier")
    except ZeroDivisionError:
        print("la division par zéro n'est pas possible")
    else:
        print(divEntier(x,y))


if __name__ == '__main__':
    sys.exit(main())