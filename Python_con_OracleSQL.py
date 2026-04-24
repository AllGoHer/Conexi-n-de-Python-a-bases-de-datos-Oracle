import oracledb

try:
    conexion=oracledb.connect(
    user='PYTHON01',
    password='123456',
    dsn='loclahost/xe')
except Exception as err:
    print('Error en la conexion a la base', err)
else:
    print('Conectado a Oracle Database', conexion.vesion)


try:
    cur_01=conexion.cursor()
    insert_datos='''insert into prueba values(
    'primer codigo', 1001)'''
    cur_01.execute(insert_datos)
except Exception as err:
    print('Error insertando datos', err)
else: 
    print('Datos insertando correctamente!')
    conexion.commit()
#crea_tabla='''create table prueba
#campo1 varchar2(40),
#campo2 int not null)'''
#cur_01.execute(crea_tabla)

conexion.close()



