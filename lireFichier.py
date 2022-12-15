import pandas as pd
import os

# Ouvrir le fichier en lecture seule
file = open('MEGALITE_FRANCAIS_bi/A/Abbot,_Edwin-Flatland.pdf.seg.bi', "r")

# utilisez readline() pour lire la première ligne
line = file.readline()
while line:
    print(line)
    # utilisez readline() pour lire la ligne suivante
    line = file.readline()
file.close()


