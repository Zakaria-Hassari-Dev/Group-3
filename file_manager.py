# file_manager.py

class FileManager:
    def __init__(self, file_path):
        """Initialise le chemin du fichier."""
        self.file_path = file_path

    def read_file(self):
        """Lit le contenu du fichier et le retourne sous forme de liste."""
        with open(self.file_path, 'r', encoding='utf-8') as file:
            return file.readlines()

    def write_to_file(self, data):
        """Écrit des données dans le fichier."""
        with open(self.file_path, 'a', encoding='utf-8') as file:
            file.write(data + '\n')

    def count_lines(self):
        """Retourne le nombre de lignes dans le fichier."""
        with open(self.file_path, 'r', encoding='utf-8') as file:
            return sum(1 for line in file)

    def search_keyword(self, keyword):
        """Recherche un mot-clé dans le fichier et retourne les lignes correspondantes."""
        with open(self.file_path, 'r', encoding='utf-8') as file:
            return [line for line in file if keyword in line]
