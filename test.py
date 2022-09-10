
import uuid
import time
import sys
import os

print(" _____ _     _      _____       _    _____ _          ")
print("|  _  |_|___| |_   |  _  |___ _| |  | __  | |_ _ ___  ")
print("|   __| |   | '_|  |     |   | . |  | __ -| | | | -_| ")
print("|__|  |_|_|_|_,_|  |__|__|_|_|___|  |_____|_|___|___| ")
print(" ____              _                   ")              
print("|    \ ___ _ _ ___| |___ ___ ___ ___ ___             ")
print("|  |  | -_| | | -_| | . | . | -_|  _|_ -|            ")
print("|____/|___|\_/|___|_|___|  _|___|_| |___|            ")
print("                        |_|                          ")
print("")
print("CERTIFICATE GENRATOR | v 0.0.1")


genrated_certificate_path = os.getcwd() + '/genrated-certificates'
if os.path.exists(genrated_certificate_path):
    print("genrated certificate path exists")
else:
    os.mkdir("genrated-certificates")
    print("genrated certificate path created successfully")