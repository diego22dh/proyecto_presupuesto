# README

Este repositorio contiene un proyecto que utiliza una base de datos en Airtable (https://airtable.com/invite/l?inviteId=invYN1HDU5VryPu23&inviteToken=f15ebf979a586b0777b44698a2761c218051cf44be220ec6a11baa87b7e8b0c6&utm_medium=email&utm_source=product_team&utm_content=transactional-alerts)  para actualizar una base de datos SQLite y generar un archivo Power BI.

## Descripción del proyecto

El objetivo de este proyecto es automatizar la actualización de una base de datos SQLite y generar un archivo Power BI utilizando los datos de una base en Airtable.

El proceso se divide en dos partes principales:

1. Actualización de la base de datos SQLite: Se utiliza un script de Python llamado `Presupuesto_auth_token.py` para conectarse a la base en Airtable y obtener los datos actualizados. Luego, estos datos se procesan y se actualiza la base de datos SQLite llamada `Presupuesto.db` con la información correspondiente.

2. Generación del archivo Power BI: Una vez que la base de datos SQLite ha sido actualizada, se utiliza la aplicación ODBC Data sources para conectarla con Power BI. Esto permite importar los datos actualizados y generar un archivo de visualización y análisis en Power BI llamado `Presupuesto Power BI Ejemplo`.

La herramienta se puede descargar desde http://www.ch-werner.de/sqliteodbc/

## Requisitos previos

Antes de ejecutar este proyecto, asegúrate de tener instalados los siguientes componentes:

- Python: Versión 3.x o superior.
- Bibliotecas de Python: Asegúrate de tener instaladas todas las bibliotecas requeridas por el script `Presupuesto_auth_token.py`. Puedes encontrar las dependencias en el archivo `requirements.txt` en este repositorio.

## Configuración

Sigue los pasos a continuación para configurar correctamente el proyecto:

1. Clona este repositorio en tu máquina local.
2. Crea una base de datos SQLite llamada `Presupuesto.db`.
3. Configura el script `Presupuesto_auth_token.py` con la dirección de la base en Airtable. Puedes encontrar el enlace en la sección de introducción de este archivo README.
4. Asegúrate de tener las credenciales de acceso necesarias para la base en Airtable.
5. Configura la aplicación ODBC Data sources para que se conecte a la base de datos SQLite `Presupuesto.db`.
6. Verifica que Power BI esté instalado en tu máquina.

## Uso

Sigue los pasos a continuación para utilizar este proyecto:

1. Ejecuta el script `Presupuesto_auth_token.py` en tu entorno Python. Este script se conectará a la base en Airtable, obtendrá los datos actualizados y los actualizará en la base de datos SQLite `Presupuesto.db`.
2. Abre la aplicación ODBC Data sources y verifica que esté conectada correctamente a la base de datos SQLite `Presupuesto.db`.
3. Abre el archivo `Presupuesto Power BI Ejemplo` en Power BI para visualizar y analizar los datos actualizados.

## Contribución

Si deseas contribuir a este proyecto, puedes seguir estos pasos:

1. Haz un fork de este repositorio y clónalo en tu máquina local.
2. Crea una rama para tu contribución: `git checkout -b nombre-de-tu-rama`.
3. Realiza los cambios y mejoras necesarias.
4. Realiza un commit de tus cambios: `git commit -m "Descripción de tus cambios"`.
5. Envía tus cambios al repositorio remoto: `git push origin nombre-de-tu-rama`.
6. Abre una solicitud de extracción en GitHub para que revisemos tus cambios.

## Problemas y preguntas

Si tienes algún problema o pregunta relacionada con este proyecto, por favor, abre un nuevo problema en la sección de "Issues" de este repositorio. Haremos todo lo posible para ayudarte.

## Licencia

Este proyecto está licenciado bajo la [MIT License](LICENSE).