from django.test import TestCase

# Prueba unitaria Users
from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomUserTests(TestCase):
    # Prueba creación de usuario
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='john',
            email='johndoe@gmail.com',
            password='testpass123')
        self.assertEqual(user.username, 'john')
        self.assertEqual(user.email, 'johndoe@gmail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    
    # Prueba creación de super usuario
    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='superadmin',
            email='superadmin@email.com',
            password='testpass123')
        self.assertEqual(admin_user.username, 'superadmin')
        self.assertEqual(admin_user.email, 'superadmin@email.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
