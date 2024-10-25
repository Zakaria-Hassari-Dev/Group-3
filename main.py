from file_manager import FileManager

def main():
    log_file = 'log.txt'  # Assurez-vous que ce fichier existe dans le même répertoire.
    manager = FileManager(log_file)

    # Lire le contenu du fichier
    manager.read_file()

    # Écrire une nouvelle ligne dans le fichier
    new_log = "INFO: Une nouvelle entrée dans le log."
    manager.write_to_file(new_log)

    # Compter les lignes
    line_count = manager.count_lines()
    print(f"Nombre de lignes dans le fichier {log_file} : {line_count}")

    # Rechercher un mot-clé
    manager.search_keyword("ERROR")
    manager.search_keyword("INFO")

if __name__ == "__main__":
    main()
