import pandas as pd
import os


#construction_phrase('exemple.txt')
#construction_phrase('../MEGALITE_FRANCAIS_bi/A/Abbot,_Edwin-Flatland.pdf.seg.bi')

def lire_fichier(fichier):
    colonnes = ["Mots", "Occurence"]
    file = pd.read_csv(fichier , names= colonnes , sep = '\t', dtype={'Mots': str, 'Occurence': float}, header=None, index_col=None, encoding='latin-1')
    file=file.tail(-1)

    return file


def fusion_de_fichier(rep):
    liste_mots = pd.DataFrame(columns= ['Mots' ,'Occurence'])
    liste_mots_res = pd.DataFrame(columns= ['Mots' ,'Occurence'])
    res = pd.DataFrame(columns= ['Mots' ,'Occurence'])
    
    liste_mots["Occurence"] = liste_mots["Occurence"].astype(str).astype(int)
    res["Occurence"] = res["Occurence"].astype(str).astype(int)
    liste_mots_res["Occurence"] = liste_mots_res["Occurence"].astype(str).astype(int)


    cpt = 0
    for path, subdirs, files in os.walk(rep):
        for name in files:
            fichier = os.path.join(path, name)
            print(fichier)
            res = lire_fichier(fichier)
            if liste_mots.empty:
                liste_mots = res
            else:
                for i in range(1,len(liste_mots)):
                    for j in range(1,len(res)):
                        #print('=============================================\n ',liste_mots['Mots'][i] ," =======================>",res['Mots'][j])
                        #print('=============================================\n ',liste_mots['Occurence'][i] ," =======================>",res['Occurence'][j])
                        if liste_mots['Mots'][i] == res['Mots'][j]:
                            rep = liste_mots['Occurence'][i] + res['Occurence'][j]
                            #print("Mots ",liste_mots['Mots'][i])

                            liste_mots.loc[i, 'Occurence'] = int(rep)
                            
                            res.loc[j, 'Mots'] = ''
                            res.loc[j, 'Occurence'] = ''
                            cpt += 1

                res = res[res['Mots'] != '']
                liste_mots_res = pd.concat([liste_mots,res], ignore_index=True)

    print(liste_mots_res.shape)
    liste_mots_res.to_csv("fusion.csv", header=False, columns= ['Mots' ,'Occurence'], index=False, sep=' ')

#fusion_de_fichier("exemple")


def fusion_rapide():
    
    ## permet de fusionner tous les fichier du magalite
    #os.system("cat MEGALITE_FRANCAIS_bi/*/*.bi > rep_fusion/fichier_fusion.bi")
    
    ## permet de supprimer les mots 'BIGRAMAS'
    #os.system("sed '/\BIGRAMAS$/d' rep_fusion/fichier_fusion.bi >> rep_fusion/fusion.bi")

    liste_mots = pd.DataFrame(columns= ['Mots' ,'Occurence'])
    liste_mots = lire_fichier("rep_fusion/fusion.bi")

    liste_mots["Occurence"] = liste_mots["Occurence"].astype(str).astype(int)
    #print(liste_mots.shape)
    liste_mots = liste_mots.groupby(['Mots'])[["Occurence"]].sum()
    print(liste_mots.shape)
    print(liste_mots.head())
    liste_mots.to_csv("rep_fusion/fusion_concat.csv", header=False, index=False, sep=' ')
fusion_rapide()