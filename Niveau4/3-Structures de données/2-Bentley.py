input()
liste = [int(x) for x in input().split()]

def maxi(i, j):
    """
    return (mg, m, md, tt)
    mg: maximum de la sous-suite commençant à gauche
    m: maximum de la sous-suite
    md: maximum de la sous-suite commençant à droite
    tt: la somme de la suite
    """
    if i+1 == j:
        return liste[i], liste[i], liste[i], liste[i]
    else:
        g_mg, g_m, g_md, g_tt = maxi(i, int((i+j)/2))
        d_mg, d_m, d_md, d_tt = maxi(int((i+j)/2), j)
        mg = max(g_mg, g_tt+d_mg)
        m = max(g_m, d_m, g_md+d_mg)
        md = max(g_md+d_tt, d_md)
        tt = g_tt + d_tt
        return mg, m, md, tt

mg, m, md, tt = maxi(0, len(liste))
print(max(m, 0))
