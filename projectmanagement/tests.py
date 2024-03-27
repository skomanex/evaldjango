
# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse
from .models import Utilisateur


class LoginTests(TestCase):
    def setUp(self):
        # Création d'un utilisateur pour les tests
        Utilisateur.objects.create(nom='test', mail='test@example.com', mdp='test')

    def test_login_valid(self):
        # Test de connexion avec des identifiants valides
        client = Client()
        response = client.post(reverse('login'), {'email': 'test@example.com', 'password': 'test'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('pageutilisateur', args=['test']))

    def test_login_invalid(self):
        # Test de connexion avec des identifiants invalides
        client = Client()
        response = client.post(reverse('login'), {'email': 'test@example.com', 'password': 'wrong'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        self.assertEqual(response.context['error'], 'Mauvais mail ou mot de passe')
