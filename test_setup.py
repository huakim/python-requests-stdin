import requests_stdin
import requests
s = requests.Session()
s.mount('stdin://', requests_stdin.StdinAdapter())

def test_request():
  assert s.get('text://some_text').text == 'some_text'
