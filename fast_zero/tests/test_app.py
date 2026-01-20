from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}


def test_helloworldhtml_deve_retornar_html():
    client = TestClient(app)

    response = client.get('/helloworldhtml')

    assert response.status_code == HTTPStatus.OK
    assert 'text/html' in response.headers.get('content-type', '')
    assert '<html' in response.text.lower()
