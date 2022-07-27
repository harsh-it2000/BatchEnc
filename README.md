# BatchEnc
Uses novel design of custom made encryption/decryption algorithm under hybrid cryptography using concepts of RSA and Cubic Pell’s Equation which would provide a reliable way secure batch files.The derivation of the equation and its Encryption and Decryption algorithms and implementations along with the numerical instance are included in the repostitory.
In this project we will be proposing an algorithm for hybrid cryptography which serves as a reliable and secure 
way to keep the data uninformed to the intruder or any other outside middle man. The project aims to take the 
data as input and produce a meaning secure files which could be stored separately on two different geological 
locations and be safe. While these files are accessed by the concerned authority or system, calculations and 
manipulations are again performed with the help of a key from the file itself to produce the original data from
normal use. The derivation of the equation and its Encryption and Decryption algorithms along with the numerical 
instance are mentioned as a hand written document below.
We have accumulated multiple newly published papers with new and improved cryptographic algorithms for 
different scenarios, which are usually comparing themselves with the ones that they have improved upon or only 
with the most famous ones. So in this project we will also try to compare all the aspects of these algorithms (all 
that we can) with one that we have prepared. The comparing scenarios will include performance, security and 
resource utilization of these particular algorithms


# ALGORITHM
1. So as mentioned above in the derivation we have generated the formulae which we are supposed to take into 
consideration.
2. Take the initial file which is to be encrypted 
3. Read the file 
4. Now based on the formulae generated encrypt the file no. by no. 
5. Two different files are generated which is to be taken care of.
6. A key is generated for carrying out symmetric encryption as by the formulae
a. key = int ((max(L1) **2 + max(L2) **2) / (max(L1) + max(L2)))
b. where L1 and L2 are the CT1 and CT2 taken under consideration.
7. File is passed through this formula
a. ct1x.append(ct1a[i]^key)
8. Later when the files are required to be decrypted again they are fed by the formulae
a. ct2a.append(int (L2[i]) + int (mine2))
b. ct2x.append(ct2a[i]^key)


#

![image](https://user-images.githubusercontent.com/55338027/181191603-95b4b063-cac8-49cd-a0f2-3b7fc76d9b00.png)
