# Guia completa de APIS


- [hackeando apps](#hackeando-apks-android-apps)
- [creando una api en aws](#aws-lambdas-python)
    - lambdas
    - cronjobs
    - dynamodb
- [ejemplos](#ejemplos-de--apis)

## Hackeando APKS (android apps) 

Hackeando apps de android podemos obtener los endopoints de algunas apis privadas. Primero necesitamos bajar el `apk` de la aplicacion, luego debemos modificar la applicacion para poder interceptar y decofidicar los requests que realiza.

[ejemplo](https://gist.github.com/unoexperto/80694ccaed6dadc304ad5b8196cbbd2c)

### instalar apktool

https://ibotpeaches.github.io/Apktool/install/

* Download apktool from https://ibotpeaches.github.io/Apktool/
* Unpack apk file: `apktool d app.apk`
* Modify AndroidManifest.xml by adding `android:networkSecurityConfig="@xml/network_security_config"` attribute to `application` element.
* Create file /res/xml/network_security_config.xml with following content:
```
<?xml version="1.0" encoding="utf-8"?>
<network-security-config>
    <base-config>
        <trust-anchors>
            <certificates src="system" />
            <certificates src="user" />
        </trust-anchors>
    </base-config>
</network-security-config>
```
* Build patched apk: `apktool b app -o app_patched.apk`
* error `Resource is not public` see https://github.com/iBotPeaches/Apktool/issues/810
* If you see error 'android:localeConfig in Manifest' see https://github.com/iBotPeaches/Apktool/issues/2756#issuecomment-1059370741
* If you see followint error try running `java -jar /home/expert/work/tools/apktool.jar empty-framework-dir --force` or run `b` command with parameter `--use-aapt2`
```
W: invalid resource directory name: /home/expert/Downloads/Zzzzzz/Zzzzzz_v0.0.0/res navigation
brut.androlib.AndrolibException: brut.common.BrutException: could not exec (exit code = 1): [/tmp/brut_util_Jar_5815054990385134498.tmp, p, --forced-package-id, 127, --min-sdk-version, 23, --target-sdk-version, 29, --version-code, 226000400, --version-name, 226.000.0, --no-version-vectors, -F, /tmp/APKTOOL14466004687895005947.tmp, -e, /tmp/APKTOOL4388243966604401097.tmp, -0, arsc, -I, /home/expert/.local/share/apktool/framework/1.apk, -S, /home/expert/Downloads/Zzzzzz/Zzzzzz_v0.0.0/res, -M, /home/expert/Downloads/Zzzzzz/Zzzzzz_v0.0.0/AndroidManifest.xml]
* ~~Generate keys to sign apk: `keytool -genkey -alias keys -keystore keys -keyalg RSA -keysize 2048 -validity 10000 # password`~~
* ~~Sign apk file: `jarsigner -verbose -keystore keys /home/expert/Downloads/lancet/flixster_patched.apk keys`~~
* Old method of signing with jarsigner produces apk that new version of Android refuses to install.
Please use: `java -jar uber-apk-signer.jar --apks /path/to/apks` from [here](https://github.com/unoexperto/uber-apk-signer).
* If necessary convert apk to jar for further analysis: `d2j-dex2jar.sh net.flixster.android-9.1.3@APK4Fun.com.apk`
* To find what cyphers suites are supported by remote server calls: `nmap --script ssl-enum-ciphers -p 443 youtubei.googleapis.com` or `sslscan youtubei.googleapis.com`
* To check what cypher suites your client supports query https://www.howsmyssl.com/a/check
```

Luego de tener la version parcheada y firmada, la instalamos en nuetro celular

### PCAPdroid

Usaremos esta aplicacion de android para interceptar los pedidos, con esto podremos encontrar los endpoints de los recursos que nos interesan y el metodo de autentificacion si es que lo tiene.

## Crear una API

Luego de tener los endpoints de la api, vamos crear nuestra propia API para. Una manera sencilla es usar AWS lambdas

### AWS lambdas (python)


Creemos nuestra primera lambda:


- nombre: testAPI
- runtime: python3.10
- arq: x86_64
- crear nuevo rol: ✔️
- habilitar URL de la función: ✔️
- autorizacion: NONE
- habilitar CORS: ✔️

Si hacemos un requests GET o entramos con el navegador a la [url](https://kz2zmo73y7zxtre5vp7avoukcu0vvjgz.lambda-url.us-east-1.on.aws/) de la funcion, deberiamos ver el siguiente mensaje:

```
'Hello from Lambda!'
```

En la solapa **codigo**, podemos modificar el comportamiento de nuestra lambda

```python
import json

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hola ya cree y modifique una lambda!')
    }
```


### CloudWatch

AWS ofrece un sistema para centralizar todos los logs, nos conviene setear nuestra lambda para poder visualizar logs. Para esto vamos a permisos y creamos un nuevo rol (ponemos un nombre como rolMILAMBDA para no olvidarnos). Luego debemos asignarle permisos full cloudwatch logs.

Ahora cuando probemos o ejecutemos nuestra lambda, quedaran guardado nuestros logs.

### DynamoDB

Podemos usar esta base de datos para alamanacenar data scrapeada


### Cron jobs

Queremos que este requests y update de la tabla se realice de manera automatica cada 15 minutos. Para esto vamos a usar un trigger (un disparador), vamos al dashboard de nuestra lambda y vamos a `+ add trigger`.

Seleccionamos:

```
EventBridge (CloudWatch Events)
```

Y luego configuramos **Create a new rule** y le asignamos un nombre:

- Rule name: `ELNOMBREQUEQUIERASPARAELTRIGGER`

Y por ultimo definimos cada cuanto se va a ejecutar nuestra lambda, como ejemplo uso 15 minutos:

- Schedule expression: `rate(15 minutes)`


## Ejemplos de  apis:


### Comparativa precios (Dia% , Carrefour, ChangoMas)
```
https://7pyngmccwa.execute-api.us-east-1.amazonaws.com/default/apitest?q=chocolate
``` 


### Trenes


