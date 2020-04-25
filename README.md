# Traitement champi

contient les codes utilisés pour faire des extractions simples depuis les gpickle

## Distribution masse

Calcul de la distribution de la masse dans le thalle. Attention à bien mettre le centre repéré sur ImageJ dans Distribution_masse 

1. Distribution_masse.py => Sort des fichiers texte, contenant la position X et Y et la longueur de chaque segment défini par un noeud de degré 2
1. plot_distribution_masse.py => Plot and save la distribution

## Comptage noeuds

1. get_all_nodes.py => appelle comptage_noeud et sort un fichier appelé all_nodes.txt contenant les listes de noeud avec leurs degré
1. comptage_noeuds.py => sous programme de get_all_nodes.py
1. read_time.py => va chercher s'il existe dans log.txt la série temporelle correspondant aux temps experimentaux et l'ajoute dans all_nodes.txt.
