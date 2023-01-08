import pandas as pd
import chardet
import os

#cette fonction permet de lire dans un fichier et le met dans un Dataframe
def lire_fichier(fichier):
    colonnes = ["Mots", "Occurence"]
    file = pd.read_table(fichier , names= colonnes , sep = '\t', dtype={'Mots': str, 'Occurence': float}, header=None, index_col=None, encoding='utf-8')
    file=file.tail(-1)

    return file

#cette fonction permet de faire la fusion des bigrammes du megalite-fr
def fusion_rapide():
    ## permet de fusionner tous les fichier du magalite-fr
    # os.system("cat ../MEGALITE_FRANCAIS_bi/*/*.bi > rep_fusion/fichier_fusion.bi")
    
    ## permet de supprimer les mots 'BIGRAMAS' dans le fichier
    # os.system("sed '/\BIGRAMAS$/d' rep_fusion/fichier_fusion.bi >> rep_fusion/fusion_concat.txt")    
    
    liste_mots = pd.DataFrame(columns= ['Mots' ,'Occurence'])
    liste_mots1 = pd.DataFrame(columns= ['Mots' ,'Occurence'])

    liste_mots = lire_fichier("fusions/fusion_concat.txt")

    #print(liste_mots.shape)
    #permet de fusionner les bigrammes et faire la somme des occurrences
    liste_mots1 = liste_mots.groupby(['Mots'])["Occurence"].sum()
    #print(liste_mots1.head())
    liste_mots1.to_csv("fusions/fusion_finale.txt", header=False, sep= '\t')
    
fusion_rapide()