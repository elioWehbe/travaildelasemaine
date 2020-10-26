#1-nombre d'element
def len_Rec(seq):
    if seq==[]:
        return 0
    else:
        return 1 +len_Rec(seq[1:])

seq=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(len_Rec(seq))
#2-somme d'une liste
def soeRec(L):
    if L==[]: return 0
    return L[-1]+soeRec(L[:-1])
L=[1,2,3,5]
print(soeRec(L))
#3-moyenne d'une sequence
def moySoeRec(liste):
    nbre=len_Rec(liste)
    if nbre==0: return 0
    else: return (liste[-1]+soeRec(liste[:-1]))/nbre
liste=[1,2,3,5]
print(moySoeRec(liste))
#4-inserer un element dans une liste triee
import bisect
def insert(list, n):
    bisect.insort(list, n)
    return list
list = [1, 2, 4]
n = 3
print(insert(list, n))
#5-Tri d’une liste
def quick_sort(l):
    if len(l) <= 1:
        return l
    else:
        return quick_sort([e for e in l[1:] if e <= l[0]]) + [l[0]] +\
            quick_sort([e for e in l[1:] if e > l[0]])
liste=[5,2,7,10]
print(quick_sort(liste))





