Python y SQL

Desarrollo de GUI básica con libreria TKINTER de python y manipulación de datos con sentencias SQL en una conexión a DB de SQLite.

En relación a la librería se usan recursos como: Frame, Label, Button, Treeview, Scrollbar, Toplevel para el desarrollo de la interfaz. Básicamente consite en ingresar datos a una Base de Datos, y poder manipular la data con sentencias SQL.

En relación al uso de la Base de datos, se usa un sistema de gestión de bases de datos (DBMS). Algunos lenguajes de programación vienen con módulos que puede usar para interactuar con un DBMS, mientras que otros requieren el uso de paquetes de terceros. Se desarrollará una aplicación sencilla para interactuar con las bases de datos SQLite.

SQLite es una biblioteca de código abierto en lenguaje C que implementa un motor de base de datos SQL pequeño, rápido, autónomo, de alta confiabilidad y con todas las funciones. Más información en www.sqlite.org

Se pretende con esta aplicación aprender a como:
1. Conectarse a una DB con un sistema de administración de Python
2. Interactuar con DB SQLite
3. Realizar consultas comunes desde una aplicación en Python
4. Desarrollar aplicaciones utilizando un script en Python

Nota: Para conectarse a MySQL y/o PostgreSQL se requieren servidores en funcionamiento para ejecutar los scripts.

SQLite es probablemente la base de datos más sencilla para conectarse con una aplicación Python, ya que no necesita instalar ningún módulo externo Python SQL para hacerlo. De manera predeterminada, su instalación de Python contiene una biblioteca Python SQL llamada "sqlite3" que puede usar para interactuar con una base de datos SQLite.

Además, las bases de datos SQLite no tienen servidor y son independientes , ya que leen y escriben datos en un archivo. Esto significa que, a diferencia de MySQL y PostgreSQL, ¡ni siquiera necesita instalar y ejecutar un servidor SQLite para realizar operaciones de base de datos!