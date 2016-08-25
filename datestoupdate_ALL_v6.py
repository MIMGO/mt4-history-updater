print 'miguel.garcia.oton@gmail.com\nTwitter: miguelmgo'
import os
import time


print('\nEste programa toma los datos de 2 archivos. Y genera Los datos nuevos\
 modificados con el formato\nmod_AA_XXXXXX')
print('1. Datos de las precios que vamos a modificar.\
\nEstos han de empezar por AA_XXXXXX. Donde XXXXX es el par.\nEjemplo: AA_EURUSD60\n')
print ('2.Los datos de las fechas que queremos modificar, este archivo ha de empezar\
 por el Symbol y su nombre ha de seguir este formato:\nEURUSD_toupdate.csv\n')
print ('Su formato interno ha de ser este\n2008.01.22	1.44154\n')
raw_input('Si el proceso da error, verifica los pasos anteriores.\nPress ay key to continue\n')

# 1 -- Creo un diccionario con las fechas que se ha nde modificar y su valor
start_time = time.time()
file_names = ('AUDCAD_toupdate.csv','AUDCHF_toupdate','AUDJPY_toupdate.csv','AUDNZD_toupdate.csv','AUDUSD_toupdate.csv',
'CADCHF_toupdate.csv','CADJPY_toupdate.csv','CHFJPY_toupdate.csv','EURAUD_toupdate.csv','EURCAD_toupdate.csv','EURCHF_toupdate.csv',
'EURGBP_toupdate.csv','EURJPY_toupdate.csv','EURNZD_toupdate.csv','EURUSD_toupdate.csv','GBPAUD_toupdate.csv','GBPCAD_toupdate.csv',
'GBPCHF_toupdate.csv','GBPJPY_toupdate.csv','GBPNZD_toupdate.csv','GBPUSD_toupdate.csv','NZDJPY_toupdate.csv','NZDUSD_toupdate.csv',
'USDCAD_toupdate.csv','USDCHF_toupdate.csv','USDJPY_toupdate.csv','EURJPY_toupdate.csv') # Archivo con las fechas malas

#fname = name + '.csv'
contador = 0
for file_name in file_names:
    print file_name
    try:
        manf_data = open(file_name, 'r')
    except:
        print 'Nombre de archivo de origen de datos no valido o archivo no encontrado\n'
        #quit()
        continue
    symbol = file_name.split('_')
    symbol = symbol[0]
    print symbol

    dictdata = dict()

    for line in manf_data:
        line = line.split(';')
        date = line[0] # determina el dia. Revisarlo con el archivo original
        price = line[1] # determina el precio. Revisarlo con el archivo original
        price = price[:len(price)-1] #para quitar el salto de linea
        #print 'El dia ', date, ' el precio del activo era ', price
        dictdata[date] = price


    # 2 -- Extraigo los nombre de los archivos que quiero modificar.
    # Almaceno en una lista names
    names =list()
    for root, dirs, files in os.walk(".", topdown=True):
        for name in files:
            name = (os.path.join(root, name))
            if name.startswith('.\AA_'+ symbol):
                name = name.replace(".\\","")
                #print name
                names.append(name)
    # 3 -- Abro cada uno de los archivos que estan en names
    for name in names:
        print 'Nombre de archivo a modificar ', name
        try:
            fh = open(name)
        except:
            print 'Nombre de archivo a modificar NO VALIDO'
            #continue
            raw_input('press')
        new_file = 'mod_' + name
        print 'Nuevo archivo con los datos modificados ', new_file
        manf = open(new_file, 'wb') #CREAMOS EL ARCHIVO FINAL MODIFICADO
        manf.close()

    #----------------------------------------------------------------------
        for line2 in fh:
            full_line = line2
            line2 = line2.split(',')
            date2 = line2[0] # buscamos la fecha en el archivo a modificar
            contador = contador + 1
            if date2 in dictdata: # si la fecha esta en el archivo la escribimos
                hour2 = line2[1]
                #print date2, hour2, price, 'paso 2'
                manf = open(new_file, 'a') #ABRIMOS EL ARCHIVO EN MODO ANADIR
                manf.write(date2)
                manf.write(',')
                manf.write(hour2)
                manf.write(',')
                manf.write(dictdata[date2])
                manf.write(',')
                manf.write(dictdata[date2])
                manf.write(',')
                manf.write(dictdata[date2])
                manf.write(',')
                manf.write(dictdata[date2])
                manf.write(',')
                manf.write('000')
                manf.write('\n')
            else:
                manf = open(new_file, 'a') #ABRIMOS EL ARCHIVO EN MODO ANADIR
                manf.write(full_line)
                #manf.close()
        manf.close()


print 'FIN'
print contador
# calcular el tiempo de ejecucion del proceso 2
print '\n---------------------------------------'
localtime = time.asctime( time.localtime(time.time()))
print "\n---------------------------------------\nHora de finalizacion del proceso :", localtime
print("Duracion del proceso \n---------------- %s seconds---------------- " % (time.time() - start_time)) #medir el tiempo de ejecucion
j = raw_input('Press any key to finish')
