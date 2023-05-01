import requests as rq
import pandas as pd
import time
from datetime import datetime



class API:
  def __init__(self):
    self.url_base='https://7pyngmccwa.execute-api.us-east-1.amazonaws.com/default/apitest?q='
    self.data=pd.DataFrame(columns=['id', 'query', 'name', 'price', 'url', 'seller','fecha'])

  def get(self,producto):
    dt = datetime.now()
    df=pd.DataFrame.from_dict(rq.get(self.url_base+producto).json(),orient='index')
    time.sleep(0.1)
    df.loc[:,'query']=producto
    df.loc[:,'fecha']=dt.strftime('%y-%m-%d')
    self.data=pd.concat([self.data,df])
 
api=API()


api.get('criollitas')

api.get('galletitas melba')

api.get('arroz gallo 1kg')

api.get('harina trigo 1kg blancaflor 000')


api.get('harina de maiz')

api.get('fideos tallarin matarazzo')

api.get('papa negra 1kg')

api.get('batata 1kg')

api.get('azucar ledesma')

api.get('mermelada Campagnola')

api.get('lenteja 500')

api.get('cebolla 1kg')

api.get('banana')

api.get('carne picada')

api.get('pate')

api.get('paleta cocida')

api.get('huevos blanco')

api.get('leche entera serenisima')

api.get('queso casancrem')

api.get('yoghurt entero')

api.get('manteca serenisima')

api.get('aceite cocinero girasol')

api.get('coca cola 1,75')

api.get('heineken 473')

api.get('celusal')

api.get('mayona hellmans')

api.get('vinagre menoyo')

api.get('cafe molido cabrales 500')

api.get('yerba mate taragui')

api.data.to_csv('data.csv',index=False)