import string

def chiffre(var: str):
    A = 3
    B = 7
    dico = {}
    alpha = string.ascii_lowercase
    for elem, i in enumerate(alpha):
        dico[i] = elem

    chiffre = []
    for char in var:
        if char in dico:
            cal = (A * dico[char] + B) % 26
            chiffre.append(list(dico.keys())[list(dico.values()).index(cal)])

    return chiffre


def find(a,b):
    c = 0 
    for i in range(26):
        if(a*i)%26 == 1:
            c = i
    return c, (-b)*c


def dechiffre(chiffre: list):
    A_inv = 9  
    B = 7
    dico = {}
    alpha = string.ascii_lowercase
    for elem, i in enumerate(alpha):
        dico[elem] = i  

    texte_clair = ''
    for cal in chiffre:
        char_index = (A_inv * (cal - B)) % 26
        texte_clair += dico[char_index]

    return texte_clair

chiffre_texte = [10, 23, 20, 8, 23, 15, 6, 9]
texte_clair = dechiffre(chiffre_texte)


    

   



if__name__='__main__'

print(chiffre("bonjours"))
print(texte_clair)


