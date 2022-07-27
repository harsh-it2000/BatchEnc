import random
import os
import time

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def delete():
    if os.path.exists("file1.txt"):
        os.remove("file1.txt")
    if os.path.exists("encrypted.txt"):
        os.remove("encrypted.txt")
    if os.path.exists("decrypted.txt"):
        os.remove("decrypted.txt")


def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi//e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + phi


def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True


def generate_key_pair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    # n = pq
    n = p * q

    # Phi is the totient of n
    phi = (p-1) * (q-1)

    # Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)

    # Use Euclid's Algorithm to verify that e and phi(n) are coprime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    # Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, phi)

    # Return public and private key_pair
    # Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))


def encrypt(pk, plaintext):
    # Unpack the key into it's components
    key, n = pk
    # Convert each letter in the plaintext to numbers based on the character using a^b mod m
    cipher = [pow(ord(char), key, n) for char in plaintext]
    # Return the array of bytes
    return cipher


def decrypt(pk, ciphertext):
    # Unpack the key into its components
    key, n = pk
    # Generate the plaintext based on the ciphertext and key using a^b mod m
    aux = [str(pow(char, key, n)) for char in ciphertext]
    # Return the array of bytes as a string
    plain = [chr(int(char2)) for char2 in aux]
    return ''.join(plain)


if __name__ == '__main__':
    '''
    Detect if the script is being run directly by the user
    '''

    p = 23
    q = 19
    n = p*q

    public, private = generate_key_pair(p, q)

    # Creating list for generating random numbers
    list = list(range(n))

    # Generating File file1
    W = 2700000  # Initialising value to generate value of different file size
    f = open("file1", "w+")
    for i in range(W):
        f.write("%d " % random.choice(list))
    f.close()

    # File Accessing file1
    access_file = open("file1", 'r')
    yourResult = [line.split(' ') for line in access_file.readlines()]
    L = yourResult[0][0:W]

    text_file = open("file1", "r")
    data = text_file.read()
    text_file.close()

    start = time.time()
    # encryption through public keys, decryption through private keys
    encrypted_msg = encrypt(public, data)
    print("Encryption Period : " + str(time.time() - start))

    e = open("encrypted", "w+")
    for element in encrypted_msg:
        e.write("" + str(element))
    e.close()

    print("key", n)

    start = time.time()
    decryped_msg = decrypt(private, encrypted_msg)
    print("Decryption Period : " + str(time.time() - start))
    d = open("decrypted", "w+");
    for element in decryped_msg:
        d.write(element)
    d.close()