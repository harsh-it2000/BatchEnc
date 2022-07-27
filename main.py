# importing necessary libraries
import random
import os
import time

# Deleting the file if already exists
from typing import TextIO

def delete():
    if os.path.exists("file1.txt"):
        os.remove("file1.txt")
    if os.path.exists("ct1.txt"):
        os.remove("ct1.txt")
    if os.path.exists("ct2.txt"):
        os.remove("ct2.txt")
    if os.path.exists("dt.txt"):
        os.remove("dt.txt")
    if os.path.exists("ct1k.txt"):
        os.remove("ct1k.txt")
    if os.path.exists("ct1x.txt"):
        os.remove("ct1x.txt")
    if os.path.exists("ct2k.txt"):
        os.remove("ct2k.txt")
    if os.path.exists("ct2x.txt"):
        os.remove("ct2x.txt")


# predefined values for generation of RSA cryptography
x = 9
y = 2
r = 91
p = 23
q = 19
n = p * q
phi = (p - 1) * (q - 1)
e = 3

# Opening of the text files
h = open("ct1", "w+")
g = open("ct2", "w+")
j = open("dt", "w+")


# Function for encryption
def process(m):
    alpha = (x + phi) ** 3 - r * (y + e) ** 3
    M = m
    ct1 = M ** (alpha % phi) % n
    ct2 = M ** (r % phi) % n
    h.write("%d " % ct1)
    g.write("%d " % ct2)


# Function for decryption
def decrypt(a, b):
    a = int(a)
    b = int(b)
    dt1 = (a * b ** (((e ** 3) % phi + (3 * y ** 2 * e) % phi + (3 * y * e ** 2) % phi) % phi)) % n
    j.write("%d " % dt1)


# Creating list for generating random numbers
list = list(range(n))

# Generating File file1
W = 2700  # Initialising value to generate value of different file size
f = open("file1", "w+")
for i in range(W):
    f.write("%d " % random.choice(list))
f.close()

# File Accessing file1
access_file = open("file1", 'r')
yourResult = [line.split(' ') for line in access_file.readlines()]
L = yourResult[0][0:W]
# ---------------------------------------------------------------------

# ENCRYPTING INITIALLY TAKEN FILE
start = time.time()

for i in range(W):
    process(int(L[i]))

h.close()
g.close()
print("Encryption Period : " + str(time.time() - start))

access_file1 = open("ct1", 'r')
yourResult1 = [line.split(' ') for line in access_file1.readlines()]
L1 = yourResult1[0][0:W]
access_file2 = open("ct2", 'r')
yourResult2 = [line.split(' ') for line in access_file2.readlines()]
L2 = yourResult2[0][0:W]

# ---------------------------------------------------------------------

for i in range(W):
    L1[i] = int(L1[i])
    L2[i] = int(L2[i])

# GENERATION OF KEYS FOR SYYMETRIC SECTION
key = int((max(L1) ** 2 + max(L2) ** 2) / (max(L1) + max(L2)))
# GENERATED KEY

# ----------------------------------------------------------------------

# SYMMETRIC ENCRYPTION FOR CT1
ct1a = []
ct1x = []                                               #Stores cipher text ct1 after symm key enc
mine = max(L1)

for i in range(W):
    ct1a.append(int(L1[i]) + int(mine))

print("key", key)

for i in range(W):
    ct1x.append(ct1a[i] ^ key)

minx = int(mine) ^ key
m = open("ct1k", "w+")
m.write("%d" % int(minx))
m.close()
k = open("ct1x", "w+")
for i in ct1x:
    k.write("%d " % int(i))
k.close()
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# SYMMETRIC ENCRYPTION FOR CT2
ct2a = []
ct2x = []                                               #Stores cipher text ct2 after symm key enc
mine2 = max(L2)
for i in range(W):
    ct2a.append(int(L2[i]) + int(mine2))
for i in range(W):
    ct2x.append(ct2a[i] ^ key)
minx2 = int(mine2) ^ key
m = open("ct2k", "w+")
m.write("%d" % int(minx2))
m.close()
k = open("ct2x", "w+")
for i in ct2x:
    k.write("%d " % int(i))
k.close()
#---------------------------------------------------------------------

# DECRYPTION PART
mind = int(minx) ^ key
for i in range(W):
    ct1x[i] = (ct1x[i] ^ key) - mind
mind2 = int(minx2) ^ key
for i in range(W):
    ct2x[i] = (ct2x[i] ^ key) - mind2
start2 = time.time()
for i in range(W):
    decrypt(ct1x[i], ct2x[i])
j.close()
print("Decryption Period : " + str(time.time() - start2))
access_file3 = open("dt", 'r')
yourResult3 = [line.split(' ') for line in access_file3.readlines()]
DT = yourResult3[0][0:W]
# FINAL VALUES ARE STORED IN THE DECRYPTED TEXT FILE
