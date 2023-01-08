import pandas as pd
import numpy as np
import os
import re

#Lire dans le fichier Table Associative
def lire_fichier_TableAssociative(etiquette):
    listeLignes = []
    liste = []
    try:
        file = open('TableAssociative','r')
        while 1:
            ligne = file.readline()
            #on stock tous les mots dans le tableau
            listeLignes = ligne.split('\t')
            if listeLignes[0] == etiquette:
                liste = listeLignes #on recupere que les mots qui appartienne à la même etiquette
            if(ligne == ''):
                break
    except:
        print("Le fichier n'existe pas")
    return liste #on retourne la liste

#lire dans le fichier anti dictionnaire
def lire_fichier_anti_dictionnaire():
    liste = []
    listeLignes = []
    try:
        file = open('Antidictionnaire.txt','r')
        while 1:
            ligne = file.readline()
            listeLignes = ligne.split('\n')
            liste.append(listeLignes[0]) #on mets dans le tableau tous les mots
            if(ligne == ''):
                break
    except:
        print("Le fichier n'existe pas")
    return liste

#lire dans le fichier embedding
def lire_fichier_embeding(mots):
    ## suppression des caractère spécieux dans le fichier
    #os.system("sed 's/\]//g ; s/,//g ;' ../embeddings-Fr.txt >> embeddings-Fr.txt")
    
    #on créer un dataframe avec colonne mots et vecteurs
    my_cols = ['Mots', 'Vecteur']
    liste_mots = pd.read_table('embeddings-Fr.txt', sep = '\t',names=my_cols, header = None, encoding='utf8', engine="python")
    #print(liste_mots.head())
    vecteur_context = []

    #on recupere le vecteur du mots contexte
    def vecteur_context(context):
        for i in range(len(liste_mots)):
            if liste_mots['Mots'][i] == context:
                vect1 = liste_mots['Vecteur'][i]
                results = re.split(r' ', vect1)
        results2 = [float(i) for i in results if i]
        return results2
    vecteur_context = vecteur_context('colère') #il faut donné le mots contexte ici

    #on recupere aussi le vecteur du mots à remplacer dans la phrase
    def vecteur_du_mots(context):
        for i in range(len(liste_mots)):
            if liste_mots['Mots'][i] == context:
                vect1 = liste_mots['Vecteur'][i]
                results = re.split(r' ', vect1)
        results2 = [float(i) for i in results if i]
        return results2
    vecteur_mots = vecteur_du_mots(mots)

    #on calcule la distance entre le mots contexte et le mots à remplacé
    vector_dot_product = np.dot(vecteur_context, vecteur_mots)
    arccos = np.arccos(vector_dot_product / (np.linalg.norm(vecteur_context) * np.linalg.norm(vecteur_mots)))
    angle = np.degrees(arccos)
    #on return le vecteur du contexte, la liste des mots et angle du mots à changé
    return vecteur_context,liste_mots,angle
    
#cette fonction permet de calculer l'angle entre deux mots
def calcule_distance(liste_mots, liste_mots_associative, vecteur_context, dist):
    #print(liste_mots.head())
    indice = 0
    word = ""
    distance = 1000
    for i in range(len(liste_mots)):
        for j in liste_mots_associative:
            if liste_mots['Mots'][i] == j:
                vect1 = liste_mots['Vecteur'][i]
                vecteur_mots = re.split(r' ', vect1)
                results = [float(i) for i in vecteur_mots if i]

                #calcule de l'angle
                vector_dot_product = np.dot(vecteur_context, results)
                arccos = np.arccos(vector_dot_product / (np.linalg.norm(vecteur_context) * np.linalg.norm(results)))
                angle = np.degrees(arccos)
                
                #on trouve l'angle la plus petite
                dist = angle - dist
                if abs(dist) < distance:
                    distance = abs(dist)
                    indice = i
                    word = liste_mots['Mots'][i]
    return indice, word

#cette fonction permet de remplacer un mots dans une phrase
def remplacer_mots(search_text, replace_text):
    with open('entre.txt', 'r') as file:
        data = file.read()
        data = data.replace(search_text, replace_text)

    with open('entre.txt', 'w') as file:
        file.write(data)

def lecture_fichier():

    colonnes = ['Mots' ,'Lemme','EtiquettePOS','Score']
    column = ['Mots']
    liste_mots = pd.DataFrame(columns= colonnes)
    liste_mots = pd.read_table('testResult.txt' , names= colonnes , sep = ' ', dtype={'Mots': str, 'Lemme': str, 'EtiquettePOS':str, 'Score':float}, header=None, index_col=None, encoding='utf8')
    
    liste_antidico = lire_fichier_anti_dictionnaire()

    
    liste = []
    liste_etiquette = []
    for i in range(len(liste_mots)):
        if liste_mots['Mots'][i] !='.' and liste_mots['Mots'][i] not in liste_antidico: #on verifie si le mots n'est pas dans l'antidictionnaire
            liste.append(liste_mots['Mots'][i])
            liste_etiquette.append(liste_mots['EtiquettePOS'][i])
    
    #pour chaque mots dans la phrase on calcule l'angle avec tous les mots et on le remplace par le mots le plus proche
    for i in range(len(liste_etiquette)):
        mots = liste[i]
        liste_mots_associative = lire_fichier_TableAssociative(liste_etiquette[i])
        vecteur_context, liste_m, dist = lire_fichier_embeding(mots)
        indice, world = calcule_distance(liste_m, liste_mots_associative, vecteur_context, dist)
        #print(indice, world)
        remplacer_mots(liste[i], world)
    
lecture_fichier()

