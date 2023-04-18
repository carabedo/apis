import base64
import json
import requests as r
import pandas as pd
import sys

def get_dia(producto):
    url_base='https://diaonline.supermercadosdia.com.ar/_v/segment/graphql/v1?workspace=master&maxAge=long&appsEtag=remove&domain=store&locale=es-AR&__bindingId=39bdf81c-0d1f-4400-9510-96377195dd22&operationName=bdwrecommendation&variables=%7B%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%22e40934becf10756c349f9ec5f702ba3297e65a0606c3b8afe48355e1d1fe7d4c%22%2C%22sender%22%3A%22braindw.braindw-io%400.x%22%2C%22provider%22%3A%22braindw.braindw-io%400.x%22%7D%2C%22variables%22%3A%22'
    var={'input': {'sessionId': '{"last_products":[],"last_sku":[],"last_category":null,"shelfId":"BDW-SR-Carrusel-1","clientHash":"dia_io_produccion_xe2tf","isDebug":null,"vtexCookie":"b98e10b6-8db8-41f3-832a-ce6f161d7c93","path":"%2Fmilanesas","cartProducts":[],"queryTerm":"chocolatada","lastProductsExito":[],"lastProductsMercado":[],"categoriesFilterString":""}',
    'strategy': 'BEST_SELLERS',
    'input': {'type': {'primary': 'ANONYMOUS_USER'},
    'values': ['search/aceitunas']},
    'recommendation': {}}}
    var['input']['input']['values'][0]='search/' + producto
    query64=base64.b64encode(json.dumps(var).encode()).decode()
    url_end='%22%7D'
    url=url_base+query64+url_end
    response=r.get(url)
    data=response.json()
    lista=data['data']['bdwrecommendation']['response']['recommendations'][0]['recommended']
    productos=[]
    for x in lista:
        producto={}
        producto['id']=x['productReference']
        producto['name']=x['productName']
        producto['list_high']=x['priceRange']['listPrice']['highPrice']
        producto['list_low']=x['priceRange']['listPrice']['lowPrice']
        producto['sell_high']=x['priceRange']['sellingPrice']['highPrice']
        producto['sell_low']=x['priceRange']['sellingPrice']['lowPrice']
        producto['url']='https://diaonline.supermercadosdia.com.ar/'+x['link']+'/p'
        producto['seller']='dia'
        productos.append(producto)
    return pd.DataFrame(productos),lista,data

def get_dia2(producto,num=10):
  url_base='https://diaonline.supermercadosdia.com.ar/_v/segment/graphql/v1?workspace=master&maxAge=medium&appsEtag=remove&domain=store&locale=es-AR&operationName=productSuggestions&variables=%7B%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%2291879f1bb1a15f6c82df6fa9e1e98a090cd8eabe497b969507bf30f7a213c415%22%2C%22sender%22%3A%22vtex.store-resources%400.x%22%2C%22provider%22%3A%22vtex.search-graphql%400.x%22%7D%2C%22variables%22%3A%22'
  var={'productOriginVtex': True,
      'simulationBehavior': 'default',
      'hideUnavailableItems': False,
      'fullText': 'milanesas',
      'count': num,
      'shippingOptions': []}
  var['fullText']= producto
  query64=base64.b64encode(json.dumps(var).encode()).decode()
  url_end='%22%7D'
  url=url_base+query64+url_end
  response=r.get(url)
  data=response.json()
  lista=data['data']['productSuggestions']['products']
  productos=[]
  for x in lista:
    producto={}
    producto['id']=x['items'][0]['ean']
    producto['name']=x['productName']
    producto['list_high']=x['priceRange']['listPrice']['highPrice']
    producto['list_low']=x['priceRange']['listPrice']['lowPrice']
    producto['sell_high']=x['priceRange']['sellingPrice']['highPrice']
    producto['sell_low']=x['priceRange']['sellingPrice']['lowPrice']
    producto['url']='https://diaonline.supermercadosdia.com.ar/'+x['link']+'/p'
    producto['seller']='dia'
    productos.append(producto)
  return pd.DataFrame(productos),lista,data

def get_carrefour(producto,num=10):
  url_base='https://www.carrefour.com.ar/_v/segment/graphql/v1?workspace=master&maxAge=medium&appsEtag=remove&domain=store&locale=es-AR&__bindingId=ecd0c46c-3b2a-4fe1-aae0-6080b7240f9b&operationName=productSuggestions&variables=%7B%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%2291879f1bb1a15f6c82df6fa9e1e98a090cd8eabe497b969507bf30f7a213c415%22%2C%22sender%22%3A%22vtex.store-resources%400.x%22%2C%22provider%22%3A%22vtex.search-graphql%400.x%22%7D%2C%22variables%22%3A%22'
  var={'productOriginVtex': True,
  'simulationBehavior': 'default',
  'hideUnavailableItems': False,
  'fullText': 'cerveza',
  'count': num,
  'shippingOptions': []}
  var['fullText']= producto
  query64=base64.b64encode(json.dumps(var).encode()).decode()
  url_end='%22%7D'
  url=url_base+query64+url_end
  response=r.get(url)
  data=response.json()
  lista=data['data']['productSuggestions']['products']
  productos=[]
  url_base='https://www.carrefour.com.ar/'
  for x in lista:
    producto={}
    producto['id']=get_ean(x)
    producto['name']=x['productName']
    producto['list_high']=x['priceRange']['listPrice']['highPrice']
    producto['list_low']=x['priceRange']['listPrice']['lowPrice']
    producto['sell_high']=x['priceRange']['sellingPrice']['highPrice']
    producto['sell_low']=x['priceRange']['sellingPrice']['lowPrice']
    producto['url']=url_base+x['link'].split('com.br/')[1]
    producto['seller']='carrefour'
    productos.append(producto)
  return pd.DataFrame(productos),lista,data

def get_ean(x):
    try:
      ean=[y for y in x['properties'] if y['name'] =='EAN'][0]['values'][0]
      return ean
    except:
      return x['productId']

def get_changomas(producto,num=10):
  url_base='https://www.masonline.com.ar/_v/segment/graphql/v1?workspace=master&maxAge=medium&appsEtag=remove&domain=store&locale=es-AR&operationName=productSuggestions&variables=%7B%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%2291879f1bb1a15f6c82df6fa9e1e98a090cd8eabe497b969507bf30f7a213c415%22%2C%22sender%22%3A%22vtex.store-resources%400.x%22%2C%22provider%22%3A%22vtex.search-graphql%400.x%22%7D%2C%22variables%22%3A%22'
  var={'productOriginVtex': True,
  'simulationBehavior': 'default',
  'hideUnavailableItems': False,
  'fullText': 'cerveza quilmes litro ',
  'count': 10,
  'shippingOptions': []}
  var['fullText']= producto
  query64=base64.b64encode(json.dumps(var).encode()).decode()
  url_end='%22%7D'
  url=url_base+query64+url_end
  response=r.get(url)
  data=response.json()
  lista=data['data']['productSuggestions']['products']
  productos=[]
  url_base='https://www.masonline.com.ar/' 
  for x in lista:
    producto={}
    producto['id']=x['items'][0]['ean']
    producto['name']=x['productName']
    producto['list_high']=x['priceRange']['listPrice']['highPrice']
    producto['list_low']=x['priceRange']['listPrice']['lowPrice']
    producto['sell_high']=x['priceRange']['sellingPrice']['highPrice']
    producto['sell_low']=x['priceRange']['sellingPrice']['lowPrice']
    producto['url']=url_base+x['link'].split('com.br/')[1]
    producto['seller']='chango'
    productos.append(producto)
  return pd.DataFrame(productos),lista,data


def comparar3(producto,num=50):
  df1,lista1,data1=get_dia2(producto,num)
  df2,lista2,data2=get_carrefour(producto,num)
  df3,lista3,data3=get_changomas(producto,num)
  df1.id=df1.id.astype('int')
  df2.id=df2.id.astype('int')
  df3.id=df3.id.astype('int')
  dfm=df1.merge(df2,on='id',suffixes=('_dia','_carrefour'),how='inner')
  df_compare=dfm.drop([ 'list_high_dia', 'list_low_dia', 'sell_high_dia',
          'url_dia', 'seller_dia', 'name_carrefour',
        'list_high_carrefour', 'list_low_carrefour', 'sell_high_carrefour', 'url_carrefour', 'seller_carrefour'],axis=1)
  df_compare.columns=['id', 'name', 'precio_dia', 'precio_carrefour']
  dfm2=df_compare.merge(df3,on='id',how='inner')
  df_compare2=dfm2.drop(['name_y', 'list_high',
      'list_low', 'sell_high', 'url', 'seller'],axis=1)
  df_compare2.columns=['id', 'name', 'precio_dia', 'precio_carrefour','precio_chango']
  return df1,df2,df3,df_compare2
  
producto=sys.argv[1]

df_comparacion=comparar3(producto)

print(df_comparacion)