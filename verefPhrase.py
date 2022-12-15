import pandas as pd
import os

os.system('analyze -f fr.cfg < test.txt > testResult.txt')
print("Le fichier a été généré !!!")

def genereSens():
    colonnes = ['Mots' ,'Lemme','EtiquettePOS','Score']
    liste_mots = pd.DataFrame(columns= colonnes)
    liste_mots = pd.read_table('testResult.txt' , names= colonnes , sep = ' ', dtype={'Mots': str, 'Lemme': str, 'EtiquettePOS':str, 'Score':float}, header=None, index_col=None, encoding='utf8')

    #print(liste_mots.head())
    print(liste_mots.shape)
    print(liste_mots)
genereSens()



