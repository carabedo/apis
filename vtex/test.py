import sys
from main import *

producto=sys.argv[1]
print('buscando', producto )

try:
    df,lista,dat=get_dia(producto)
    print('dia%', len(lista),' productos')
except:
    print('fallo dia%')

try:
    df,lista,dat=get_dia2(producto)
    print('dia%', len(lista),' productos')
except:
    print('fallo dia2')

try:
    df,lista,dat=get_carrefour(producto)
    print('carrefour', len(lista),' productos')
except:
    print('fallo carrefour')
try:
    df,lista,dat=get_changomas(producto)
    print('chango', len(lista),' productos')
except:
    print('fallo chango')