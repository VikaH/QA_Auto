import pytest
import requests


@pytest.mark.http
def test_first_request():
    r = requests.get('https://api.github.com/zen')
    print (r.text)

@pytest.mark.http
def test_second_request():
    r = requests.get('https://api.github.com/users/defunkt') # { "text": 'jdlkfjgblkdfjgh' }
    body = r.json()
    headers = r.headers
    # print (f"Response Body is {r.json()}")
    # print (f"Response Status code is {r.status_code}")

    assert body['name'] == 'Chris Wanstrath'
    assert body['public_repos'] == 107
    assert r.status_code == 200
    assert headers['Server'] == 'github.com'
    
    if r.status_code == 200:
       print (f"Response Status code is {r.status_code}")
    else:
        print (r.status_code)
    print (f"Response Headers is {r.headers}")

@pytest.mark.http
def test_status_code_request():
    r = requests.get('https://api.github.com/users/Sergii_butenko')
    
    assert r.status_code == 404