# Api Trenes

## Comportamiento de la APP:

cercanas? si

horarios/groups (grupo == sentido)

```
GET /v1/estaciones/271/horarios?fields=results%28desde%28id%2CnombreCorto%2Cllegada%2Csegundos%2Canden%29%2Chasta%28id%2CnombreCorto%2Cllegada%2Csegundos%2Canden%29%2Csalida%2Cservicio%28id%2Cramal%2Ctren%2Cformacion%28id%2Cposicion%29%2Cascendente%2Crealtime%2CtipoServicio%2Cdestino%28nombreCorto%29%29%29&lineas=5&cabeceraFinal=190&limit=3 HTTP/1.1 
Host: apiarribos.sofse.gob.ar 
Connection: Keep-Alive 
Accept-Encoding: gzip 
User-Agent: okhttp/3.11.0 
If-None-Match: W/"698-FeBaZJ/fHCOtlMKldBOFpk7lvk4"
```

## Endpoints

Estos son los endpoints que figuran en la app de android.

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
