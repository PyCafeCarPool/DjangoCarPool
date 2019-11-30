from django.test import TestCase
from django.contrib.auth.models import User

import pytest

pytestmark = pytest.mark.django_db

@pytest.mark.django_db
class TestUsers:
    pytestmark = pytest.mark.django_db
    def test_an_admin_view(admin_client):
        response = admin_client.get('/admin/')
        assert response.status_code == 200
