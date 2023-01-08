import pandas as pd
import os

#cette fonction permet de lire dans un fichier et le mettre dans un dataframe
def lire_fichier_fusion(fichier):
    colonnes = ['Mots1', 'Mots2', 'Occurence']
    file = pd.read_table(fichier , sep = ' |\t', names= colonnes, dtype = {'Mots1': str, 'Mots': str, 'Occurence': float}, header=None, engine="python")
    #print(file.head())
    file=file.tail(-1)
    return file

liste_mots = pd.DataFrame(columns= ['Mots1', 'Mots2' ,'Occurence'])

liste_mots = lire_fichier_fusion("rep_fusion/fusion_finale.txt")
liste_mots['Mots1'] = liste_mots['Mots1'].str.replace('"',"")
liste_mots['Mots2'] = liste_mots['Mots2'].str.replace('"',"")
#print(liste_mots.head())

#cette fonction permet generer une phrase avec les bigramme vers la gauche
def bigramme_avant(mots):
    max = -1
    indice = 0
    for i in range(1,len(liste_mots)):
        if liste_mots['Mots1'][i] == mots:
            if liste_mots['Occurence'][i] > max: #on trouve l'occurence le plus grands
                max =  liste_mots['Occurence'][i]
                indice = i
    lettre = liste_mots['Mots2'][indice]
    liste_mots.loc[indice, "Occurence"] = 0 #on met l'occurence à null pour ne pas que le bigrammes se repette
    return lettre

#cette fonction permet generer une phrase avec les bigramme vers la droite
def bigramme_apres(mots):
    max = -1
    indice = 0
    for i in range(1,len(liste_mots)):
        if liste_mots['Mots2'][i] == mots:
            if liste_mots['Occurence'][i] > max: #on trouve l'occurence le plus grands
                max =  liste_mots['Occurence'][i]
                indice = i
    lettre = liste_mots['Mots1'][indice]
    liste_mots.loc[indice, "Occurence"] = 0 #on met l'occurence à null pour ne pas que le bigrammes se repette
    return lettre

def construction_phrase(mots):

    lettre = mots
    lettre1 = mots
    table_mots_avant = []
    table_mots_apres = []
    table_mots = []
    table_mots_avant.append(lettre)
    res = ""
    res1 = ""

    #pour recuperer les mots avant
    for i in range(0,7):
        res = bigramme_avant(lettre)
        table_mots_avant.append(res)
        lettre = res
        #print(res)
    
    #pour recuperer les mots après
    for i in range(0,3):
        res1 = bigramme_apres(lettre1)
        table_mots_apres.append(res1)
        lettre1 = res1
        #print(res1)
    
    table_mots_apres.reverse()

    #on ajoute dans table_mots des deux tables genérées
    for i in table_mots_apres:
        table_mots.append(i)
    for i in table_mots_avant:
        table_mots.append(i)

    #on mets le contenue du tableau dans un string
    print("------------------------ Resultat ---------------------------")
    result = ""
    for i in table_mots:
        result =  result + i + " "
    print(result)
    #écriture du resultat dans le fichier
    fichier = open("resultat.txt", "w")
    fichier.write(result)
    fichier.close()
construction_phrase("dansé")


#fichier testResult : pour mettre les résultats de freeling
os.system('analyze -f fr.cfg < resultat.txt > testResult.txt')
print("Le fichier a été généré !!!")

def genereSens():
    colonnes = ['Mots' ,'Lemme','EtiquettePOS','Score']
    liste_mots = pd.DataFrame(columns= colonnes)
    liste_mots = pd.read_table('testResult.txt' , names= colonnes , sep = ' ', dtype={'Mots': str, 'Lemme': str, 'EtiquettePOS':str, 'Score':float}, header=None, index_col=None, encoding='utf8')

    #print(liste_mots.head())
    #print(liste_mots.shape)
    print(liste_mots)
genereSens()


def verifierLexique():
    colonnes = ['Mots' ,'Lemme','EtiquettePOS','Score']
    liste_mots = pd.DataFrame(columns= colonnes)
    liste_mots = pd.read_table('testResult.txt' , names= colonnes , sep = ' ', dtype={'Mots': str, 'Lemme': str, 'EtiquettePOS':str, 'Score':float}, header=None, index_col=None, encoding='utf8')
    
    options = ['PP1CSN0', 'SP']

    rslt_df = liste_mots[liste_mots['EtiquettePOS'].isin(options)]
    #print('\nResult dataframe :\n', rslt_df)
    
    liste=[]

    #Conditions pour vérifier la phrase grammaticalement
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

    result = ""
    for i in liste:
        result =  result + i + " "
    print(result)
    #écriture du resultat dans le fichier
    fichier = open("resultat.txt", "w")
    fichier.write(result)
    fichier.close()

    #fichier testResult : pour mettre les résultats de freeling
    os.system('analyze -f fr.cfg < resultat.txt > entre.txt')

verifierLexique()
