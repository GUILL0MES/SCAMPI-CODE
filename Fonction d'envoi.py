import paramiko

def envoi_des_donnees() :
    # Configuration de la connexion
    hostname = 'adresse_IP_du_serveur'
    port = 22  # Port SSH par défaut
    username = 'nom_utilisateur'
    password = 'mot_de_passe'

    # Création d'une instance SSHClient
    client = paramiko.SSHClient()

    # Connexion au serveur
    client.connect(hostname, port, username, password)

    # Utilisation de la connexion précédemment établie
    sftp = client.open_sftp()

    # Upload d'un fichier
    sftp.put('chemin_local/du_fichier', '/chemin_distant/du_fichier')

    # Fermeture de la connexion
    client.close()
