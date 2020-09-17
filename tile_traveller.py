# •	Markmið forritsins er að notandi komist á endastað (3,1)
# •	Við viljum spyrja notanda hvaða átt hann vill fara í (N,S,A,V) 
# •	Ef hann velur vitlaust, þá viljum við spyrja hann aftur
# •	Ef hann velur rétt þá fær hann gefnar upp nýjar leiðir sem eru í boði
# •	Þetta er endurtekið þar til hann sigrar (kemst á endastað) þá hættir forritið 

hnit_x = 1
hnit_y = 1

n = 1
s = -1
w = -1
e = 1


def nuverandi_stada(hnit_x, hnit_y):
    while sigur == False:
        str1 = input("You can travel: ", )
        if (hnit_x == 1 and hnit_y == 1):
            print("Valid directions: (N)orth")
        elif (hnit_x == 2 and hnit_y == 1):
            print("Valid direction: (N)orth")
        elif (hnit_x == 3 and hnit_y == 1):
            print("Victory!")
            sigur == True
        elif (hnit_x == 1 and hnit_y == 2):
            print("Valid direction: (N)orth or (S)outh")
        elif (hnit_x == 1 and hnit_y == 3):
            print("Valid direction: (S)outh or (E)ast")
        elif (hnit_x == 2 and hnit_y == 2):
            print("Valid direction: (S)outh or (W)est")
        elif (hnit_x == 2 and hnit_y == 3):
            print("Valid direction: (E)ast or (W)est")
        elif (hnit_x == 3 and hnit_y == 3):
            print("Valid direction: (W)est or (S)outh")
        elif (hnit_x == 3 and hnit_y == 2):
            print("Valid direction: (N)orth or (S)outh")
    return()