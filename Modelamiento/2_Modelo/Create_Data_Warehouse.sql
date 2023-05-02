-- 1. Creación nuestra base de datos
if  exists (select name from sys.databases where name='DWH_SUPERMAYORISTA') 
	begin
		use master
		alter database DWH_SUPERMAYORISTA set single_user with rollback immediate
		drop database DWH_SUPERMAYORISTA
	end

create database DWH_SUPERMAYORISTA
go

use DWH_SUPERMAYORISTA
-- 2.Creacion de las tablas de la base de datos 
-- 2.1. DIM_VENDEDOR
if object_id('DIM_VENDEDOR') is not null
	drop table DIM_VENDEDOR 

create table DIM_VENDEDOR(
	cod_vendedor char (7),
	vendedor varchar(65),
	supervisor char (7),
	primary key(cod_vendedor)
	)

insert into DIM_VENDEDOR
	select cod_vendedor, apellido_vendedor+', '+nombre_vendedor, supervisor
		from SUPERMAYORISTA.dbo.VENDEDOR 
go

-- 2.2. DIM_PRODUCTO
if object_id('DIM_PRODUCTO') is not null
	drop table DIM_PRODUCTO

create table DIM_PRODUCTO(
	cod_producto char(9),
	nombre_producto varchar(150) not null,
	categoria_producto varchar(50) not null,
	subcategoria_producto varchar(50) not null,
	precio_unitario decimal(8, 2) not null
	primary key(cod_producto)
	)

insert into DIM_PRODUCTO
	select cod_producto,nombre_producto,categoria_producto,subcategoria_producto,precio_unitario
		from SUPERMAYORISTA.dbo.PRODUCTO
go

-- 2.3. DIM_CLIENTE
if object_id('DIM_CLIENTE') is not null
	drop table DIM_CLIENTE

create table DIM_CLIENTE(
	dni_cliente char(11),
	sexo_cliente varchar(15) not null,
	fecha_nacimiento date not null,
	departamento_cliente varchar(50) not null,
	distrito_cliente varchar(50) not null,
	ubigeo_cliente varchar(10) not null,
	punto_geografico varchar(50) not null,
	primary key(dni_cliente)
	)

insert into DIM_CLIENTE
	select dni_cliente,sexo_cliente,fecha_nacimiento,departamento_cliente,distrito_cliente,ubigeo_cliente,punto_geografico
		from SUPERMAYORISTA.dbo.CLIENTE
go

-- 2.5. DIM_BANCO
if object_id('DIM_BANCO') is not null
	drop table DIM_BANCO

create table DIM_BANCO(
	cod_banco char(5),
	nombre_banco varchar(20) not null,
	comision decimal(3, 1) not null,
	primary key(cod_banco)
	)

insert into DIM_BANCO
	values('BAN01','BBVA',2.8),
		  ('BAN02','BCP',3.5),
		  ('BAN03','SCOTIABANK',2),
		  ('BAN04','INTERBANK',3),
		  ('BAN05','MIBANCO',4.2),
		  ('BAN06','CAJA HUANCAYO',3.3)
go

-- 2.6. FACT_VENTA
if object_id('FACT_VENTA') is not null
	drop table FACT_VENTA


create table FACT_VENTA(
	cod_documento char(10),
	dni_cliente char(11) foreign key references DIM_CLIENTE(dni_cliente),
	vendedor varchar(65), 
	nombre_tipo_documento varchar(20) not null,
	estado varchar(10) not null,
	fecha_venta date not null,
	cod_producto char(9) foreign key references DIM_PRODUCTO(cod_producto),
	precio_unitario decimal(8,2) ,
	cantidad int ,
	cod_banco char(5) foreign key references DIM_BANCO(cod_banco),
	)

insert into FACT_VENTA
	select v.cod_documento,v.dni_cliente,replace(v.vendedor,'Ã‘','Ñ') as vendedor,v.nombre_tipo_documento,
		   v.estado, v.fecha_venta,d.cod_producto,d.precio_unitario,d.cantidad, null as cod_banco
		from SUPERMAYORISTA.dbo.VENTA as v
			left join SUPERMAYORISTA.dbo.DETALLE_VENTA  as d
				on v.cod_documento=d.cod_documento

go

