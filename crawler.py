import urllib.request

import urllib2.request
from urllib2 import Request
content = urllib2.request.urlopen("https://www.melhorcambio.com/dolar-hoje").read()
content = str(content)
find = '<input type="hidden" value=">'
posicao  = int(content.index(find)+len(find))
dolar = content[posicao:posicao+4]

print("dolar:"+ dolar)