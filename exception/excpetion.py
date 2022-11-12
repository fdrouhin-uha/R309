import sys
#EXERCIE 1 
def divEntier(x: int, y: int) -> int:
    if x < y:
        return 0
    else:
        x = x - y
    return divEntier(x, y) + 1

def main():
    x= int(input('nombre entier: '))
    y= int(input('nombre entier: '))
    divEntier(x,y)


if __name__ == '__main__':
    sys.exit(main())