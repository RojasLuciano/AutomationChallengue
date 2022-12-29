import pytest
import requests


@pytest.mark.all
def test_departments():
    """Test get departments"""
    requestsurl = 'https://www.mercadolibre.com.ar/menu/departments'
    response = requests.request("GET", requestsurl)
    response_data = response.json()
    assert response_data.get('departments')
    assert response.status_code in (201, 200)
