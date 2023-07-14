# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 17:12:55 2023

@author: Diego
"""

import pandas as pd
import requests
import sqlite3
import json

#Defino llaves y Bases
personal_access_token = "patAn4I8UKBe05o17.732a047ce499fdd6045f1bb067fefec18fd6f79e4f9d0de286252cf8447d457d"
base_id = "appTtisK8CrUzCXHi"
base_ingresos_id = "tblXDDr6KenLtLjAf"
base_gastos_id = "tblXAgPEP7XQugdao"
base_planctas_id= "tbl6WX6KyXfeBZ10B"
base_presupuestados_id= 'tblCberAANU177KhL'
base_table_api_ingresos_url = "https://api.airtable.com/v0/{}/{}".format(base_id, base_ingresos_id)
base_table_api_gastos_url = "https://api.airtable.com/v0/{}/{}".format(base_id, base_gastos_id)
base_table_api_planctas_url = "https://api.airtable.com/v0/{}/{}".format(base_id, base_planctas_id)
base_table_api_presupuestados_url = "https://api.airtable.com/v0/{}/{}".format(base_id, base_presupuestados_id)


#Crea Headers para API
def create_headers():
    headers = {
        "Authorization": "Bearer " + personal_access_token,
        "Content-Type": "application/json",
    }
    return headers

#Trae todos los registros
def fetch_all_records(url):
    headers = create_headers()
    all_records = []

    params = {
        "pageSize": 100,  # Ajusta el tamaño de página para controlar cuántos registros se obtienen por solicitud
        "offset": None  # Inicialmente establecido en None para comenzar desde el primer registro
    }

    while True:
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        records = data.get("records", [])

        if not records:
            break

        all_records.extend(records)
        offset = data.get("offset")
        if not offset:
            break

        params["offset"] = offset

    return all_records

# Creo los df con los que voy a trabajar
ingresos_records = fetch_all_records(base_table_api_ingresos_url)
ingresos_df = pd.json_normalize(ingresos_records)

gastos_records = fetch_all_records(base_table_api_gastos_url)
gastos_df = pd.json_normalize(gastos_records)

planctas_records = fetch_all_records(base_table_api_planctas_url)
planctas_df = pd.json_normalize(planctas_records)

presupuestados_records = fetch_all_records(base_table_api_presupuestados_url)
presupuestados_df = pd.json_normalize(presupuestados_records)



####Ingresos####
#Saco columnnas que no necesito del df Ingresos
ingresos_df =ingresos_df.drop(['fields.ID', 'fields.Cliente',
        'fields.Creacion','fields.Debe', 'fields.Haber', 'fields.SALDO', 
        'fields.Plan de Cuentas',
        'fields.Concepto (from Plan de Cuentas)',
       'fields.Tipo (from Plan de Cuentas)'], axis=1)



#Paso los campos relacionados en Airtable como string 
ingresos_df['fields.Cliente (from Cliente)'] = ingresos_df['fields.Cliente (from Cliente)'].apply(lambda x: ','.join(str(e) for e in x) if isinstance(x, list) else str(x))
ingresos_df['fields.Tipo-Concepto'] = ingresos_df['fields.Tipo-Concepto'].apply(lambda x: ','.join(str(e) for e in x) if isinstance(x, list) else str(x))

####Plan Ctas###
#Saco columnnas que no necesito del df plan de cuentas
planctas_df = planctas_df.drop(['id', 'createdTime','fields.Gastos', 
       'fields.Gastos Presupuestados', 'fields.Ingresos Estudio',
       'fields.Ingresos Estudio 4'], axis=1)


####Gastos####
#Paso los campos relacionados en Airtable como string 
gastos_df['Cuenta'] = gastos_df['fields.Cuenta'].apply(lambda x: ','.join(str(e) for e in x) if isinstance(x, list) else str(x))
gastos_df['Tipo'] = gastos_df['fields.Tipo'].apply(lambda x: ','.join(str(e) for e in x) if isinstance(x, list) else str(x))
gastos_df['Tipo-Concepto'] = gastos_df['fields.Tipo-Concepto'].apply(lambda x: ','.join(str(e) for e in x) if isinstance(x, list) else str(x))

#Saco columnnas que no necesito del df Gastos
gastos_df = gastos_df.drop(['id', 'createdTime', 
        'fields.Importe', 'fields.Plan de Cuentas',
       
       'fields.Cuenta',
       'fields.Tipo',
       'fields.Tipo-Concepto'], axis=1)


####Presupuestados####
#Paso los campos relacionados en Airtable como string 

presupuestados_df['Cuenta'] = presupuestados_df['fields.Descripcion (from Cuenta)'].apply(lambda x: ','.join(str(e) for e in x) if isinstance(x, list) else str(x))
presupuestados_df['Tipo-Concepto'] = presupuestados_df['fields.Tipo-Concepto'].apply(lambda x: ','.join(str(e) for e in x) if isinstance(x, list) else str(x))

presupuestados_df = presupuestados_df.drop(['fields.Cuenta','fields.Cuenta (from Cuenta)','fields.Concepto (from Cuenta)',
                                            'fields.Tipo-Concepto'], axis=1)


#Saco columnnas que no necesito del df Gastos
presupuestados_df = presupuestados_df.drop(['fields.Descripcion (from Cuenta)'], axis=1)


### Conexion con Base de Datos####

#Conecto con BD Sqlite
con = sqlite3.connect('D:\Curso Python Albert\Avanzado\Ejemplos\Airtable\Presupuesto.db')
cursor = con.cursor()


#Mando el df al dbbrowser
gastos_df.to_sql('Gastos', con,if_exists='replace')
ingresos_df.to_sql('Ingresos', con, if_exists='replace', index = False)
planctas_df.to_sql('PlanCtas', con, if_exists='replace', index = False)
presupuestados_df.to_sql('Presupuestados', con,if_exists='replace')
