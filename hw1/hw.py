import math

def sortFunc(x,y,z):
    l = [math.ceil(x),math.ceil(y),
            math.ceil(z)]
    for i in range(len(l)):
        mi = i
        for j in range(i+1,len(l)):
            if l[j] < l[mi]:
                mi = j
        l[i], l[mi] = l[mi], l[i]
    return l

def main():
    n1 = float(input('Num 1: '))
    n2 = float(input('Num 2: '))
    n3 = float(input('Num 3: '))
    print('The ceilings of those numbers sorted are: '+
            str(sortFunc(n1,n2,n3)))

if __name__ == '__main__':
    main()
