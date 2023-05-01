# Proyecto-Supermayorista

<p align="center">
  <img src="https://media.licdn.com/dms/image/C4E22AQH1E8vrhitwaw/feedshare-shrink_800/0/1673874172503?e=2147483647&v=beta&t=jAvwaoGpwnLjnNsPox1FD-rtTqRcB_MwCyt3h5JQ5ew" width="200" height="200">
</p>

---
## Indice

- 1.[Descripción](#1-descripción)
  - 1.1.[Proyecto SUPERMAYORISTA SAC](#11-proyecto-supermayorista-sac)
  - 1.2.[Conclusión](#12-conclusión)
  - 1.3.[Puntos del negocio](#13-puntos-del-negocio)


---
## 1. Descripción
### 1.1. Proyecto SUPERMAYORISTA S.A.C.

<p align="justify">
Supermayorista es una empresa que vende productos variados de supermercado a nivel nacional donde actualmente la empresa cuenta con una base de datos de su sistema donde almacena sus productos, clientes y las ventas realizadas sin embargo el sistema solo arroja reportes operacionales donde la información no se encuentra procesada para el análisis. 
</p>
<p align="justify">
Sin embargo, la empresa Supermayorista contrato a un analista de negocio para que pudiera explotar la información de su data pero el tiempo de entrega del analista de negocio es muy lento, ya que en promedio demora por reporte solicitado entre 2 a 3 días dependiendo la dificultad del caso.
</p>
<p align="justify">
También han automatizado sus ventas desde el año 2022 a través de los canales de bancos pero pagando una comisión por cada documento de pago, dicha información les llega en un archivo plano por mes, para que puedan realizar su cierre al inicio del próximo mes.
  
Por eso mismo Supermayorista desea contratar los servicios de Datagrowth Community para implementar un Business Intelligence, Business Analitycs según sea el caso.
</p>

### 1.2. Conclusión

El gerente solicita un modelo donde la obtención de la información sea oportuna, limpia y escalable.

La información principal que desea saber la empresa es: 

1. Total de ventas por periodo.
2. Los productos más vendidos (categoría, subcategoria).
3. Los vendedores destacados.
4. Los supervisores con baja efectividad.
5. Zona con mayor venta y cantidad (Departamento, Distrito).
6. El banco más factible para solicitar un ajuste de comisión
7. El top de los vendedores que más comisionan por venta, Q(cantidad), S/ (Monto)
8. Pronosticar las ventas del 2023.
9. Estrategias para subir las ventas 2023.

### 1.3. Puntos del negocio

1. Existe dos tipos de documento que se debe conocer cómo funciona:
    - BOLETA: No tiene IGV -> Total = La suma total de producto por su cantidad.
    - FACTURA: tiene IGV -> Total = La suma total de producto por su cantidad(subtotal) + 18% de su valor subtotal
2. Comisiones de ventas por cada documento (Factura, Boleta, etc):
    - Boleta: 1.2% del total
    - Factura sin incluir IGV: 1.8% del total 
3. Comisiones adicionales por ser supervisor.
    - Muy aparte que el supervisor también es un vendedor y comisiona según el punto 2, también comisiona el 1% por cada FACTURA vendido por su equipo (el supervisor no cuenta aquí) que supere el monto de 20000 (Monto de FACTURA sin incluir el IGV).
4. La tabla VENTA tiene un campo estado, donde el registro ANULADO es una venta que no se dio, sin embargo, aparecerá en la tabla VENTA con dicho estado pero no se visualizara en la tabla DETALLE_VENTA.
5. Cada Supervisor cuenta con un equipo de 7 vendedores, donde puede obtener comisiones individualmente y comisión adicional por miembros del equipo, según condición del punto 3.
6. La tabla de comisiones que el banco cobra por cada documento de pago es:

<p align="center">
  <img src="https://github.com/Squad-Battle-4-the-top/Proyecto-Supermayorista/blob/main/images/dim_banco.png">
</p>

7.  La metadata y/o lectura del archivo plano donde se encuentra almacenado las ventas realizadas, estos puntos son los siguientes para que tengan en consideración para su análisis.

<p align="center">
  <img src="https://github.com/Squad-Battle-4-the-top/Proyecto-Supermayorista/blob/main/images/dim_banco.png">
</p>



---
