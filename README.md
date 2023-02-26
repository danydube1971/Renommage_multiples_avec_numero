# Renommage_multiples_avec_numero

Demande à l'utilisateur d'entrer un numéro de départ pour la numérotation automatique des fichiers du répertoir actuel 
sans toucher au nom du script lui-même.

Explication détaillée du script:

1. Demande à l'utilisateur d'entrer un numéro de départ pour la numérotation automatique des fichiers.
2. Utilise la fonction os.listdir() pour obtenir la liste des fichiers dans le répertoire courant.
3. Utilise une boucle for pour itérer sur chaque fichier dans la liste.
4. Vérifie si chaque élément dans la liste est un fichier avec la fonction os.path.isfile().
5. Vérifie si le nom de fichier est différent du nom du script en cours d'exécution avec filename != os.path.basename(__file__).
6. Si le fichier est différent du script, crée un nouveau nom de fichier en utilisant le numéro de départ et l'indice de la boucle.
7. Utilise la fonction os.rename() pour renommer le fichier avec le nouveau nom de fichier.
8. Affiche le nom du fichier d'origine et le nouveau nom de fichier renommé.
9. Répète les étapes 4 à 8 pour chaque fichier dans la liste.

Testé sous Linux Mint 21
