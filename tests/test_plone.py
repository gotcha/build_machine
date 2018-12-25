import pytest
import requests

from requests.exceptions import (
    ConnectionError,
)

@pytest.fixture(scope='session')
def plone_site(some_http_service):
    from requests.auth import HTTPBasicAuth
    payload = dict(site_id="Plone", default_language="fr", setup_content=True)
    payload['form.submitted'] = True
    response = requests.post(f'{some_http_service}/@@plone-addsite', data=payload, auth=HTTPBasicAuth('admin', 'admin'))
    response.raise_for_status()
    return f'{some_http_service}/Plone'

def test_something(plone_site):
    """Sample test."""
    response = requests.get(plone_site)
    response.raise_for_status()
    assert "Bienvenue" in response.text
