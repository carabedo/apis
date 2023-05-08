
import pandas as pd
import requests as rq
import datetime
import time

def get(producto):
  return pd.DataFrame.from_dict(rq.get('https://7pyngmccwa.execute-api.us-east-1.amazonaws.com/default/apitest?q='+producto).json(),orient='index')

prods=['criollitas','galletas melba','arroz gallo 1kg','harina trigo 1kg blancaflor 000','harina de maiz','fideos tallarin matarazzo','papa negra 1kg','batata 1kg','azucar ledesma','mermelada Campagnola','lenteja 500','cebolla 1kg','banana','carne picada','pate','paleta cocida','huevos blanco','leche entera serenisima','queso casancrem','yoghurt entero','manteca serenisima','aceite cocinero girasol','coca cola 1,75','heineken','celusal','mayona hellmans','vinagre menoyo','cafe molido cabrales 500','yerba mate taragui']


now=datetime.datetime.now()
date=now.strftime("%d/%m/%y")

data=[]
for x in prods:
  df=get(x)
  df['date']=date
  df['id']=df['id'].astype('str')
  df['query']=x
  data.append(df)
  time.sleep(0.2)

data=pd.concat(data)
date=now.strftime("%y-%m-%d")

data.to_csv(date+'.csv')