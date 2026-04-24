# Conexi-n-de-Python-a-bases-de-datos-Oracle  ![image](https://github.com/user-attachments/assets/6d6e0b7c-b234-4091-9c66-10c341d38dd6)  ![image](https://github.com/user-attachments/assets/0b5feaad-b023-47a7-b5be-3e16146e6d73)
_____________________________________________________________________________________________________________________________________________________________________________________________________________________________

1.	Después de haber descargado la base de datos Oracle, vamos a crear un usuario. Y luego instalamos la librería correspondiente cx_oracle.
2.	Vamos a la terminal y escribimos 

  	Pip install cx_oracle 

    Y damos enter para que descargue la librería.

3.	Ahora vamos a nuestro editor de código (VSCode) y creamos un archivo python e importamos la librería cx_oracle

   ![image](https://github.com/user-attachments/assets/1c91c443-9e00-4285-ae2a-784f49d94c75)

   Luego buscamos los parámetros de conexión de nuestra base de datos, como usuario, password, DSN o SID (ubicación de nuestra base de datos en el sistema operativo) y el alias de nuestra base de datos, que están ubicadas      en nuestro editor SQL Developer en nuestro esquema que creamos (PYTHON01) y hacemos click derecho y nos vamos a propierties.

   ![image](https://github.com/user-attachments/assets/1c33883b-0ae9-4f3d-bec0-f43d13411163)

   ![image](https://github.com/user-attachments/assets/d1b39d88-d7f0-40f6-8ced-ae45e71beeb4)

 4.	Luego continuamos en el editor de código y escribimos los siguiente:
      
   ![image](https://github.com/user-attachments/assets/d47421ac-4229-49b7-8913-12cc172e7f21)

   Para verificar que esta funcionando escribimos el siguiente código entre el print del else y conexión.

   ![image](https://github.com/user-attachments/assets/d7500474-d6d5-4d05-8693-6285fc74ebaf)

   Y en la terminal debe salir los siguiente:

   ![image](https://github.com/user-attachments/assets/24b70bc5-f78e-4c98-ba02-cfe7a3275f81)

   Cuando vamos a nuestro editor de código SQL Developer y hacemos la siguiente consulta:
   
   Select * from dual;
   
   Nos debe aparecer X.

![image](https://github.com/user-attachments/assets/d720876c-6aba-4e3a-a84e-9e17f1fb5c1a)

5.	Luego vamos a nuestro editor de código de python y crearemos la tabla para nuestra base de datos.
Ahora borramos parte del código anterior y dejamos solo la primera línea.

![image](https://github.com/user-attachments/assets/165e72f1-a870-4097-b206-8eb93471c826)

![image](https://github.com/user-attachments/assets/8f92d8bc-9d1f-49dd-8062-051a0315adeb)

Ahora empezamos a crear el código para la tabla

![image](https://github.com/user-attachments/assets/c8a85aa2-02b7-4153-a480-67c1a3f007ae)

![image](https://github.com/user-attachments/assets/e6c03795-5551-4753-8cde-e8ed01186098)

6.	Ahora para comprobar vamos a nuestra Oracle SQL Developer y hacemos la consulta:
Select * from prueba;

![image](https://github.com/user-attachments/assets/76a7119c-ed8f-4555-9c5c-a8586e59a733)

Ahora refrescamos el editor de objetos y verificamos que aparezcan las tablas

![image](https://github.com/user-attachments/assets/293aa2b6-424a-4130-b37b-357370a8869d)

7.	En el editor de código python nuevamente eliminamos o comentamos el código anterior para crear los elementos de la tabla.

![image](https://github.com/user-attachments/assets/afbdef56-cf83-45ab-9ae3-05c6c493d510)

![image](https://github.com/user-attachments/assets/bdaea398-faa7-46da-9529-87cfc322add0)

Luego ejecutamos o corremos el código y en consola debe decir lo siguiente:

![image](https://github.com/user-attachments/assets/322df391-9bdc-4b20-9c73-45efe5ea99c9)

8.	Por último, verificamos en el Oracle SQL Development y hacemos una consulta:

Select * from prueba;

![image](https://github.com/user-attachments/assets/fdb189bb-ceb6-4834-a579-722a78a3c80a)

Y ahí podemos ver que esta correctamente insertado el campo1 y campo2, el cual garantiza la correcta conexión.



   
