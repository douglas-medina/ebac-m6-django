import pytest
from django.urls import reverse
from mysite import settings

@pytest.mark.django_db
def test_post_views(pytestconfig):
    url = reverse('home')
    response = pytestconfig.get(url)
    assert response.status_code == 200
    assert response.content == 'Hello'