import base64
import json
import requests as r
import pandas as pd

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
        producto['price']=x['priceRange']['listPrice']['highPrice']
        producto['seller']='dia'
        productos.append(producto)
    return pd.DataFrame(productos),lista,data
