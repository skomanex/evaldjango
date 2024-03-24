# fake_data.py
# les données présentes ici sont importées dans les autres fichiers pour créer des sets de données avec lesquels jouer

users_data = [
    {"nom": "User1", "mdp": "password1", "mail": "user1@example.com", "estResponsable": True, "estTest": True},
    {"nom": "User2", "mdp": "password2", "mail": "user2@example.com", "estResponsable": True, "estTest": True},
    {"nom": "User3", "mdp": "password3", "mail": "user3@example.com", "estResponsable": False, "estTest": True},
    {"nom": "User4", "mdp": "password4", "mail": "user4@example.com", "estResponsable": False, "estTest": True},
    {"nom": "User5", "mdp": "password5", "mail": "user5@example.com", "estResponsable": False, "estTest": True}
]

projects_data = [
    {"nom": "Project1", "estTest": True},
    {"nom": "Project2", "estTest": True},
    {"nom": "Project3", "estTest": True}
]

tasks_data = [
    {"nom": "Task1", "description": "Description for Task1", "priorite": 1, "dateDebut": "2024-03-01", "dateFin": "2024-03-30", "statut": 1, "estTest": True},
    {"nom": "Task2", "description": "Description for Task2", "priorite": 2, "dateDebut": "2024-03-01", "dateFin": "2024-03-30", "statut": 2, "estTest": True},
    {"nom": "Task3", "description": "Description for Task3", "priorite": 3, "dateDebut": "2024-03-01", "dateFin": "2024-03-30", "statut": 0, "estTest": True},
    {"nom": "Task4", "description": "Description for Task4", "priorite": 4, "dateDebut": "2024-03-01", "dateFin": "2024-04-15", "statut": 1, "estTest": True},
    {"nom": "Task5", "description": "Description for Task5", "priorite": 5, "dateDebut": "2024-03-01", "dateFin": "2024-04-15", "statut": 2, "estTest": True},
    {"nom": "Task6", "description": "Description for Task6", "priorite": 6, "dateDebut": "2024-03-01", "dateFin": "2024-04-15", "statut": 0, "estTest": True},
    {"nom": "Task7", "description": "Description for Task7", "priorite": 7, "dateDebut": "2024-03-01", "dateFin": "2024-04-15", "statut": 1, "estTest": True}
]