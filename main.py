from PIL import Image, ImageFont, ImageDraw
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




# Global Variables
FONT_FILE = ImageFont.truetype(r'font/handwriting.ttf', 90)
FONT_COLOR = "#ef4036"

POPPINS_FONT = ImageFont.truetype(r'font/poppins.ttf', 20)
POPPINS_COLOR = "#000000"

template = Image.open(r'orange-curiospire-template.png')
WIDTH, HEIGHT = template.size


def make_certificates(name, date):

    image_source = Image.open(r'orange-curiospire-template.png')
    draw = ImageDraw.Draw(image_source)

    # Finding the width and height of the text. 
    name_width, name_height = draw.textsize(name, font=FONT_FILE)

    # Placing it in the center, then making some adjustments.
    draw.text(((WIDTH - name_width) / 2, (HEIGHT - name_height) / 2 + 150), name, fill=FONT_COLOR, font=FONT_FILE)
    draw.text((235, 883), date, fill=POPPINS_COLOR, font=POPPINS_FONT)


    # Saving the certificates in a different directory.
    image_source.save("./genrated-certificates/" + name +".png")
    print('Saving Certificate of:', name)        

if __name__ == "__main__":

    names = []
    date = input("Enter date of certificate: ")

    with open('list-of-names.txt') as f:
        for line in f:
            names.append(line.strip())
            
            
            
    for name in names:
        make_certificates(name, date)

    print(len(names), "certificates done.")