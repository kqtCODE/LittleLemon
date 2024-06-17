from django.test import TestCase
from django.urls import reverse
def test_menu_view(self):
        response = self.client.get(reverse('menu'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu.html')
        self.assertEqual(len(response.context['menus']), 4)
        self.assertEqual(len(response.context['desserts']), 1)
        self.assertEqual(len(response.context['drinks']), 1)
def test_item_view(self):
        response = self.client.get(reverse('item', args=[str(self.menu_1.pk)]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu-item.html')
        self.assertEqual(response.context['item'], self.menu_1)
        self.assertEqual(len(response.context['reviews']), 2)
def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertEqual(len(response.context['opening_hours']), 3)
        self.assertEqual(len(response.context['menus']), 4)

def test_about_view(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')
