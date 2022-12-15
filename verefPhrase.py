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



def verifierLexique():
    colonnes = ['Mots' ,'Lemme','EtiquettePOS','Score']
    liste_mots = pd.DataFrame(columns= colonnes)
    liste_mots = pd.read_table('testResult.txt' , names= colonnes , sep = ' ', dtype={'Mots': str, 'Lemme': str, 'EtiquettePOS':str, 'Score':float}, header=None, index_col=None, encoding='utf8')
    """
    options = ['PP1CSN0', 'SP']

    rslt_df = liste_mots[liste_mots['EtiquettePOS'].isin(options)]
    print('\nResult dataframe :\n', rslt_df)
    """
    liste=[]
    for i in range(0,len(liste_mots)):
        carc = liste_mots['EtiquettePOS'][i][0]
        if carc == 'P' or carc == 'D':
            liste.append(liste_mots['Mots'][i])
        if carc == 'V':
            liste.append(liste_mots['Mots'][i])
        if carc == 'N' or carc == 'C':
            liste.append(liste_mots['Mots'][i])
    print("--------------------------------------------")
    print(liste)    
  
verifierLexique()