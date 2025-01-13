# Crie um código em Python que teste se um site está acessível pelo computador usado

import urllib
import urllib.error
import urllib.request

try:
    site = urllib.request.urlopen('https://www.youtube.com/')
except urllib.error.URLError:
    print("O site não está acessível no momento.")
else:
    print("Consegui acessar o site com sucesso.")
    print(site.read())