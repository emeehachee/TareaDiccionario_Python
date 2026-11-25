import json


cadena = "nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"

linea = cadena.split("\n")

dic_personas = {}

for i in linea:  # o for i in linea[1:] (para recorrer empezando por la segunda posicion( se omite la cabecera))

    if i!=linea[0]:
        if i!="":
            datosTrabajador= i.split(";")

            datos={}

            datos['nombre']=datosTrabajador[1]
            datos['email']=datosTrabajador[2]
            datos['teléfono']=datosTrabajador[3]
            descuento = float(datosTrabajador[4])
            datos['descuento']=descuento

            if descuento>=10:
                datos['categoria']="VIP"
            else :
                datos['categoria']="Estandar"

            dic_personas[datosTrabajador[0]]= datos

#print(dic_personas)

# json.dumps(): transforma el diccionario en un texto con formato JSON para poder imprimirlo estructurado
#indent=4:(sangria) para poner 4 espacios nuevos en cada nivel hacia dentro y lo ponga en varias lineas
#ensure_ascii=False: para poder ver bien la tilde y no que la palabra telefono se vea rara
print(json.dumps(dic_personas, indent=4, ensure_ascii=False))