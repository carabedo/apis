# AWS lambdas (python)

Creemos nuestra primera lambda, una que solo va a mostrar un mensaje:

```python
import json

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hola ya cree una lambda!')
    }
```


## CloudWatch

AWS ofrece un sistema para centralizar todos los logs, nos conviene setear nuestra lambda para poder visualizar logs. Para esto vamos a permisos y creamos un nuevo rol (ponemos un nombre como rolMILAMBDA para no olvidarnos). Luego debemos asignarle permisos full cloudwatch logs.

Ahora cuando probemos o ejecutemos nuestra lambda, quedaran guardado nuestros logs.

## DynamoDB


## Cron jobs

Queremos que este requests y update de la tabla se realice de manera automatica cada 15 minutos. Para esto vamos a usar un trigger (un disparador), vamos al dashboard de nuestra lambda y vamos a `+ add trigger`.

Seleccionamos:

```
EventBridge (CloudWatch Events)
```

Y luego configuramos **Create a new rule** y le asignamos un nombre:

- Rule name: `ELNOMBREQUEQUIERASPARAELTRIGGER`

Y por ultimo definimos cada cuanto se va a ejecutar nuestra lambda, como ejemplo uso 15 minutos:

- Schedule expression: `rate(15 minutes)`


# apis


## jumbo

```
https://7pyngmccwa.execute-api.us-east-1.amazonaws.com/default/apitest?q=chocolate&n=5
``` 


Cantidad maxima de articulos 50.


## api_es

```
https://fep3c4yva3.execute-api.us-east-1.amazonaws.com/default/api_es?q=chocolate&n=5
``` 

## trenes

```java

public interface TrenesApi {
    @POST("v1/auth/authorize")
    Call<TokenResponse> authorize(@Body TokenRequest tokenRequest);

    @GET("v1/estaciones/cercanas")
    Call<PaginationContainer<CercanasResponse>> buscarCercanas(@Query("lat") Double d, @Query("lon") Double d2, @Query("radio") Integer num, @Query("limit") Integer num2, @Query("lineas") RetrofitArray<Integer> retrofitArray, @Query("ramales") RetrofitArray<Integer> retrofitArray2, @Query("exclude") RetrofitArray<Integer> retrofitArray3, @Query("orderBy") String str, @Query("fields") String str2);

    @GET("v1/estaciones/buscar")
    Call<PaginationContainer<Estacion>> buscarEstaciones(@Query("ids") RetrofitArray<Integer> retrofitArray, @Query("lineas") RetrofitArray<Integer> retrofitArray2, @Query("ramales") RetrofitArray<Integer> retrofitArray3, @Query("exclude") RetrofitArray<Integer> retrofitArray4, @Query("limit") Integer num, @Query("orderBy") String str);

    @GET("v1/estaciones/buscar")
    Call<PaginationContainer<Estacion>> buscarEstaciones(@Query("nombre") String str, @Query("lineas") RetrofitArray<Integer> retrofitArray, @Query("ramales") RetrofitArray<Integer> retrofitArray2, @Query("exclude") RetrofitArray<Integer> retrofitArray3, @Query("limit") Integer num, @Query("orderBy") String str2);

    @GET("v1/alertas")
    Call<List<AlertaResponse>> getAlertas();

    @GET("v1/lineas/{id}/alertas")
    Call<AlertaResponse> getAlertas(@Path("id") int i);

    @GET("v1/estaciones/{id}/alertas/geo")
    Call<BeaconResponse> getAlertasGeo(@Path("id") int i, @Query("token") String str);

    @GET("v1/alertas/viaje")
    Call<List<Alerta>> getAlertasViaje(@Query("desde") Integer num, @Query("hasta") Integer num2);

    @GET("v1/estaciones/{id}")
    Call<Estacion> getEstacion(@Path("id") int i);

    @GET("v1/estaciones/{id}/horarios/groups")
    Call<PaginationContainer<Group<Horario>>> getGroups(@Path("id") Integer num, @Query("fields") String str, @Query("lineas") RetrofitArray<Integer> retrofitArray);

    @GET("v1/estaciones/{id}/horarios")
    Call<PaginationContainer<Horario>> getHorarios(@Path("id") Integer num, @Query("hasta") Integer num2, @Query("fields") String str, @Query("lineas") RetrofitArray<Integer> retrofitArray, @Query("ramales") RetrofitArray<Integer> retrofitArray2, @Query("cabeceraFinal") RetrofitArray<Integer> retrofitArray3, @Query("servicio") Integer num3, @Query("limit") Integer num4);

    @GET("v1/estaciones/{id}/horarios")
    Call<PaginationContainer<Horario>> getItinerario(@Path("id") Integer num, @Query("hasta") Integer num2, @Query("fecha") String str, @Query("tipo") String str2, @Query("servicio") Integer num3, @Query("fields") String str3);

    @GET("v1/lineas")
    Call<List<LineaSimple>> getLineas();

    @GET("v1/ramales")
    Call<PaginationContainer<RamalDetalle>> getRamales(@Query("ids") RetrofitArray<Integer> retrofitArray, @Query("lineas") RetrofitArray<Integer> retrofitArray2, @Query("limit") Integer num, @Query("fields") String str);

    @POST("v1/reclamos")
    Call<ReclamosResponse> postReclamo(@Body ReclamosRequest reclamosRequest);
}
```

