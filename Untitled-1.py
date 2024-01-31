def pgcd(a, b):
    while b:
        a, b = b, a % b
    return a

def trouver_e(phi_n):
    e = 2
    while pgcd(e, phi_n) != 1:
        e += 1
    return e

def trouver_d(e, phi_n):
    d = 1
    while (d * e) % phi_n != 1:
        d += 1
    return d

def chiffrer_RSA(message, p, q):
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = trouver_e(phi_n)
    d = trouver_d(e, phi_n)

    message_chiffre = [(ord(char) ** e) % n for char in message]
    return message_chiffre

# Message à chiffrer
message = "Les maths sont l'essence même de la vie."

# Version "en nombre" du message
message_en_nombre = [76, 101, 115, 32, 109,  97, 116, 104, 115, 32, 115, 111, 110, 116, 32, 108, 39,101,
115, 115, 101, 110, 99, 101, 32, 100, 101, 32, 108, 97, 32, 118, 105, 101, 46]

# Paramètres p et q
p = 19  # Remplacez par votre valeur de p
q = 29  # Remplacez par votre valeur de q

# Chiffrer le message
message_chiffre = chiffrer_RSA(message, p, q)

# Afficher la valeur chiffrée de 76
print(f"La valeur chiffrée de 76 est : {message_chiffre[message_en_nombre.index(76)]}")
