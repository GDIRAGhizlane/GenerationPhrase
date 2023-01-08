# GenerationPhrase
Pour lancer notre programme : 

    1- il faut tout dabord installer python3 et installer la bibliothèque pandas.

    2- Pour faire la fusion 
        - il faut y avoir le Megalite-fr, pour pouvoir faire la fusion de tous les bigrammes.
        - executer la commande : python3 fusion.py

    3- Pour faire la Geration de phrase
        - il faut avoir fusionné "fusion_finale.txt" dans le repertoire "rep_fusion".
        - installer "freelling".
        - donner le mot de départ en paramètre dans la fonction "construction_phrase("dansé")"
        - executer la commande python3 generation.py

    4 - Pour changer les mots de la phrase selon le contexte
        - il faut y avoir les fichier "embeddings-Fr.txt", "TableAssociative", "Antidictionnaire.txt" dans le repertoire.
        - Donner le mots contexte dans la fonction
        - executer la commande python3 change_contexte.py

Merci !!!
