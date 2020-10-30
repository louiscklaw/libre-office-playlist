import requests

def selfTestHelloworld():
  print('_qqstocks.selfTestHelloworld')

def RequestHelloworld():
  r = requests.get('https://api.github.com/events')
  return r.text
