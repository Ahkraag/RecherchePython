# TEST rappel

a = "Waterloo, Waterloo, Waterloo, morne plaine"

b = a[1:3]
print("a[1:3] donne la sous-chaîne contenant les caractères d'indice 1 et 2 : \n",b)
c = a[4:18]
print("a[4:18] donne la sous-chaîne allant de l'index 4 à l'index 17 : \n",c)
d = a[:6]
print("a[:6] donne la sous-chaîne allant du début jusqu'à l'index 5 : \n",d)
e = a[3:]
print("a[3:] donne la sous-chaîne allant de l'index 3 jusqu'à la fin : \n",e)

# fonction de recherche textuelle


def recherche(motif, texte):
    for indice in range(len(texte) - len(motif) + 1):
        if texte[indice:indice + len(motif)] == motif:
            print("occurrence à l'indice ", indice)


def rechercheV1(motif, texte):
    res = []
    cout = 0
    for indice in range(len(texte) - len(motif) + 1):
        cout += len(motif)
        if texte[indice:indice + len(motif)] == motif:
            res.append(indice)
    print("cout : ", cout, "\n")
    return res


def rechercheV2(m, t):
    res = []
    j = len(m)
    compteur = 0
    for k in range(len(t)):
        if t[k] == m[0]:
            compteur += 1
            n = k + 1
            for o in range(1, j):
                if n >= len(t):
                    break
                if t[n] == m[o]:
                    compteur += 1
                    n += 1
                else:
                    compteur = 0
                    break
            if compteur == j:
                res.append(k)
                compteur = 0
    return res

# Test #

t = "Lorem ipsum dolor sit amet. Non quasi excepturi ad possimus ipsa aut voluptas expedita. In omnis fugit non quia quae non autem nesciunt ea dignissimos incidunt a rerum dolorem cum omnis voluptatem quo rerum galisum. Vel vero eligendi ut exercitationem quia et dolorum atque sit omnis voluptatem sit suscipit enim, Ea officia voluptatibus aut autem quidem in commodi consequatur id saepe quia. Et blanditiis repellat et tempora commodi eos porro aliquid. Vel enim culpa est aliquam nesciunt id animi necessitatibus ut galisum voluptas qui culpa cumque. Ea quod iure qui sint dolorem ut optio illo ab debitis velit eum alias aliquam ea debitis commodi. Ex eaque assumenda et praesentium commodi sit aliquid quisquam eum dignissimos consequuntur."
m = "dolor"
recherche(m, t)
print()
print("recherche V1 :", rechercheV1(m, t))
print("recherche V2 :", rechercheV2(m, t))

# Table de décalage et algorithme de Boyer-Moore

def table(m):
    dic={}
    for k in range(len(m)):
        dic[k]={}
        for i in range(k):
            if (m[i] not in dic[k]) or (dic[k][m[i]]<i):
                dic[k][m[i]]=i
    return dic

# Test #

p=table("adabrica")
for e in p:
    print(e,":",p[e])

