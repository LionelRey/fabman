from django.test import TestCase
from django.urls import reverse

from legacy.models import CheckKey
from members.models import Member, Project

from django.utils.encoding import force_text


class LegacyTests(TestCase):

    def setUp(self):
        member = Member.objects.create(name='Name', surname='Surname', visa='visa', rfid='1234')
        Member.objects.create(visa='visaStaff', rfid='5678', is_staff=True)

        CheckKey.objects.create(key='keykey')

        Project.objects.create(name='p1', member=member)
        Project.objects.create(name='p2', member=member)



    def test_user_existing(self):
        url = reverse('legacy:user', args=('1234',))
        response = self.client.get(url)
        self.assertEqual(force_text(response.content), 'visa')

    def test_user_no_existing(self):
        url = reverse('legacy:user', args=('9999',))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_user2_animator(self):
        url = reverse('legacy:user2', args=('5678',))
        response = self.client.get(url)
        self.assertJSONEqual(force_text(response.content), {"visa": "visaStaff", "animateur": True})

    def test_user2_not_animator(self):
        url = reverse('legacy:user2', args=('1234',))
        response = self.client.get(url)
        self.assertJSONEqual(force_text(response.content), {"visa": "visa", "animateur": False})

    def test_user2_not_existing(self):
        url = reverse('legacy:user2', args=('9999',))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_check_member(self):
        url = reverse('legacy:check', args=('keykey', 'Name', 'Surname'))
        response = self.client.get(url)
        self.assertEqual(force_text(response.content), 'ok')

    def test_check_member_special_chars(self):
        url = reverse('legacy:check', args=('keykey', 'Name', 'Surname  +++ ---  ... $$$'))
        response = self.client.get(url)
        self.assertEqual(force_text(response.content), 'ok')

    def test_check_member_no_ascii(self):
        url = reverse('legacy:check', args=('keykey', 'Nâme', 'Sürnâme'))
        response = self.client.get(url)
        self.assertEqual(force_text(response.content), 'ok')

    def test_check_not_a_member(self):
        url = reverse('legacy:check', args=('keykey', 'Name', 'Name'))
        response = self.client.get(url)
        self.assertEqual(force_text(response.content), 'not a member')

    def test_check_invalid_key(self):
        url = reverse('legacy:check', args=('oops', 'Name', 'Name'))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)

    def test_projects(self):
        url = reverse('legacy:projects', args=('visa',))
        response = self.client.get(url)
        self.assertJSONEqual(response.content, ['p1', 'p2'])