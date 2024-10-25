# Projet by : 
 # Zakaria Hassari / Soufian.elmezouari / Celina Chouali / Ahcen dehimi 
# Gestionnaire de Logs

Ce projet est une application web simple en Python et Flask, permettant la gestion d'un fichier de logs. L'application lit, affiche et ajoute des entrées de logs dans un fichier texte. Elle permet également de rechercher des mots-clés spécifiques dans le fichier et de supprimer des entrées de logs par mot-clé.

## Structure du projet

### 1. `file_manager.py`
Ce fichier contient la classe `FileManager`, qui gère les interactions avec le fichier de logs (`log.txt`). Elle permet de :
- Lire le fichier et retourner son contenu ligne par ligne,
- Écrire de nouvelles entrées dans le fichier,
- Compter le nombre de lignes,
- Rechercher un mot-clé spécifique dans le fichier,
- Supprimer des entrées de logs par mot-clé.

#### Méthodes de `FileManager`
- `__init__(self, file_path)`: Initialise le gestionnaire avec le chemin du fichier de logs.
- `read_file()`: Lit et retourne le contenu du fichier sous forme de liste.
- `write_to_file(data)`: Écrit une nouvelle entrée dans le fichier de logs.
- `count_lines()`: Retourne le nombre de lignes du fichier.
- `search_keyword(keyword)`: Retourne les lignes contenant le mot-clé recherché.
- `delete_entries(keyword)`: Supprime les lignes contenant le mot-clé spécifié.

### 2. `index.html`
La page HTML principale de l'interface utilisateur. Elle permet :
- D'afficher le contenu du fichier de logs,
- D'ajouter une nouvelle entrée,
- D'effectuer une recherche par mot-clé,
- De supprimer des entrées de logs par mot-clé.

### 3. `app.py`
Le fichier principal de l'application Flask. Il crée les routes et gère les interactions utilisateur.

#### Routes
- `/` (GET & POST) : Route principale de l'application. Affiche le contenu du fichier et prend en charge l'ajout d'entrées ainsi que la recherche de mots-clés et la suppression d'entrées.

### 4. `main.py`
Un fichier de script pour tester directement les fonctionnalités de `FileManager` sans passer par l'interface web.

### 5. `log.txt`
Le fichier de logs où toutes les entrées sont enregistrées. Ce fichier doit être dans le même répertoire que le projet pour que l'application fonctionne correctement.

### Prérequis
- Python 3.x
- Flask (peut être installé via `requirements.txt` ou directement)

### Comment Exécuter l'application
En terminal : 
```bash
python app.py
