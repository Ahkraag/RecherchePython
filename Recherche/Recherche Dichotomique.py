def recherche_dichot(t, v, g, d):
    if len(t) == 0:
        return None
    while True:
        if d < g:
            return None
        m = (g + d) // 2
        if t[m] > v:
            d = m - 1
        elif t[m] < v:
            g = m + 1
        else:
            return m


def recherche_dicho(t, v, g, d):
    if len(t) == 0:
        return None
    if g > d:
        return None
    m = (g + d) // 2
    if t[m] > v:
        return recherche_dicho(t, v, g, m - 1)
    elif t[m] < v:
        return recherche_dicho(t, v, m + 1, d)
    else:
        return m

# Test #

a=[0,1,2,3,4,5,6,7,8,9]
aa=[0,1,1,1,2,6,9]
aaa=[]
aaaa=[0,0,0,0,0,0]

print(recherche_dicho(a,4,0,10))
print(recherche_dicho(aa,9,0,7))
print(recherche_dicho(aaa,4,0,10))
print(recherche_dicho(aaaa,5,1,3))
