import math

#-----------------------------------1. IMPORTING FILE, CREATING LIST AND VALIDATION---------------------------------------------



file = open(input("Podaj nazwe pliku wraz z rozszerzeniem: "), "r", encoding="utf-8"); 
#file = open('text.txt', 'r', encoding='utf-8')
file.seek(0)
att_sol = []



#cutting text into the list that I will work with
for i in file.readlines():
    att_sol.append(i.split('; '))
#print(att_sol)



#dividing into two lists containing attribs and solutions
attrib = []
sol = []

for i in att_sol:
    if '#ATRYBUT' in i[0]:
        #validation
        assert len(i)==6, 'Brakuje którejś informacji w opisie atrubutu'
        assert float(i[2])>0 and float(i[2])<=1, 'Waga atrybutu nie zawiera się w przedziale (0,1>' 
        assert i[3] == 'Z' or i[3] == 'K', 'Wystąpiło inne oznaczenie w typie atrybutu'
        assert int(i[4]) in (1, 2, 3, 4, 5), 'Numer funkcji preferencji musi należeć do zbioru: {1,2,3,4,5}'
        h_tab = []
        h_tab.append(i[0].lstrip('#ATRYBUT '))
        for j in range(1, 5): 
            h_tab.append(i[j]) 
        h_tab.append(i[5].rstrip(' \n'))
        attrib.append(h_tab)
    elif '#ROZWIĄZANIE' in i[0]:
        h_tab = []
        h_tab.append(i[0].split('\t')[1].rstrip(' \n'))
    elif '#END' in i[0]:
        break
    else:
        for j in range(len(i)-1):
            h_tab.append(i[j])
        h_tab.append(i[len(i)-1].rstrip("\n"))
        sol.append(h_tab)
attrib.sort()
#print('\nAtrybuty')
#print(attrib)
#print('Rozwiazania')
#print(sol)



#validation:
#attrib numbers and weight's sum
weight = 0
for i in range(len(attrib)):
    assert int(attrib[i][0]) > 0 and int(attrib[0][0]) == 1, 'Numer atrybutu nie może być mniejszy lub równy 0 i musi zaczynać się od 1'
    weight += float(attrib[i][2]) #weight now because we are breaking out from loop before checking non existing error 
    if int(attrib[i][0]) == len(attrib): break
    assert int(attrib[i][0])+1 == int(attrib[i+1][0]), 'Któryś z numerów atrybutów się powtarza lub jakiegoś brakuje'
#print('Waga: ', weight)
#print(math.fabs(round(1-weight,3)))
#print('\nZaokrąglenie', round(1-weight,3))
assert round(1-weight,3) <= 0.005 and round(1-weight,3) >=-0.004, 'Suma wag poszczególnych atrybutów musi być równa 1 z dokładnością do 3 miejsca po przecinku'   


#first eliminating errors in attribs, then checking the number in the solutions
for i in range(len(sol)):
    assert len(attrib) == len(sol[i])-1 and int(attrib[len(attrib)-1][0]) == len(sol[i])-1, 'Liczba wymienionych atrybutów i maksymalny numer atrybutu musi się zgadzać z liczbą wartości tych atrybutów przy każdym rozwiązaniu' # -1 bc removing name of solution



#-----------------------------------2. ALGORITHM---------------------------------------------


#creating matrix with subtraction and multiplied by -1 where the type is cost
matrix_1 = [] #after substraction

for i in range(len(attrib)): #which att
    matrix_h1=[]
    for j in range(len(sol)): #row
        matrix_h2=[]
        for k in range(len(sol)): #column 
            if attrib[i][3] == 'K':
                matrix_h2.append((float(sol[j][i+1])-float(sol[k][i+1]))*-1)
            else:
                matrix_h2.append(float(sol[j][i+1])-float(sol[k][i+1]))
        matrix_h1.append(matrix_h2)
    matrix_1.append(matrix_h1)
#print('\nMacierz: ')
map(float, matrix_1) #changing type of matrixes into float from string
#print(matrix_1) #tables in the same order as attribs 1 - x
#print(len(matrix_1)) <- number of tables is same as the number of attribs, and sizes n x n (n - number of solutions)





#creating matrix containing tables after preference functions multiplied by weight
matrix_2 = [] 

#preference functions
def pref1(matrix, w):
    #print('\nPreference function 1')
    #print(matrix)
    matrix_h1=[]
    for i in matrix:
        matrix_h2=[]
        for j in i:
            if j>0:
                matrix_h2.append(1*w)
            else:
                matrix_h2.append(0*w)
        matrix_h1.append(matrix_h2)
    return matrix_h1

def pref2(matrix, q, w):
    matrix_h1=[]
    for i in matrix:
        matrix_h2=[]
        for j in i:
            if j>q:
                matrix_h2.append(1*w)
            else:
                matrix_h2.append(0)
        matrix_h1.append(matrix_h2)
    return matrix_h1

def pref3(matrix, p, w):
    matrix_h1=[]
    for i in matrix:
        matrix_h2=[]
        for j in i:
            if j>=p: 
                matrix_h2.append(1*w)
            elif j<p and j>0:
                matrix_h2.append((j/p)*w)
            else:
                matrix_h2.append(0)
        matrix_h1.append(matrix_h2)
    return matrix_h1

def pref4(matrix, q, p, w):
    matrix_h1 = []
    for i in matrix:
        matrix_h2=[]
        for j in i:
            if j>=p:
                matrix_h2.append(1*w)
            elif j>q and j<p:
                matrix_h2.append(0.5*w)
            else:
                matrix_h2.append(0)
        matrix_h1.append(matrix_h2)
    return matrix_h1


def pref5(matrix, q, p, w):
    matrix_h1=[]
    for i in matrix:
        matrix_h2=[]
        for j in i:
            if j>=p:
                matrix_h2.append(1*w)
            elif j>q and j<p:
                matrix_h2.append((j/(p-q))*w)
            else:
                matrix_h2.append(0)
        matrix_h1.append(matrix_h2)
    return matrix_h1



#using preference functions on the matrix_1
for i in attrib:
    #print('\n')
    #print(i)
    match i[4].strip(): #visual studio does not support yet this method anyway it works
        case '1':
            matrix_2.append(pref1(matrix_1[int(i[0])-1], float(i[2])))
        case '2':
            matrix_2.append(pref2(matrix_1[int(i[0])-1], float(i[5].split()[0]), float(i[2])))
        case '3':
            matrix_2.append(pref3(matrix_1[int(i[0])-1], float(i[5].split()[1]), float(i[2])))
        case '4':
            assert float(i[5].split()[0])<=float(i[5].split()[1]), 'Parametr q funkcji preferencji nie może być większy od p' #not sure in the instruction "Parametr q nie może być większy od p" is it possible them to be equal?
            matrix_2.append(pref4(matrix_1[int(i[0])-1], float(i[5].split()[0]), float(i[5].split()[1]), float(i[2])))
        case '5':
            assert float(i[5].split()[0])<=float(i[5].split()[1]), 'Parametr q funkcji preferencji nie może być większy od p'
            matrix_2.append(pref5(matrix_1[int(i[0])-1], float(i[5].split()[0]), float(i[5].split()[1]), float(i[2])))
#print('\ntables after using preference functions and multiplied by weight')
#print(matrix_2)





#netto value
netto = []


#calculating average
for i in range(len(sol)): #row/column
    n_p=0
    n_m=0
    for j in range(len(matrix_2)): #table
        for k in range(len(sol)): #columm/row
            n_p+=matrix_2[j][i][k]
            n_m+=matrix_2[j][k][i]
    #print(n_p)
    #print(n_m)
    #print(i+1, sol[i][0], 'przepływ preferencji netto', (n_p-n_m)/(len(sol)-1), sep=' ')   
    netto.append([(n_p-n_m)/(len(sol)-1), sol[i][0]])
netto.sort(reverse=True)
for i in range(len(netto)):
    print(i+1, netto[i][1], 'przepływ preferencji netto', round(netto[i][0], 2), sep=' ')
