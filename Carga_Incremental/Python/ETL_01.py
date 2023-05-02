import pyodbc
from sqlalchemy import create_engine
#pip install sqlalchemy-utils
from sqlalchemy.exc import InterfaceError

import pandas as pd 
import numpy as np
import glob
import argparse

def connection(server_name:str,data_warehouse_name:str,odbc_version:str):

    engine_dwh = create_engine(f"mssql+pyodbc://@{server_name}/{data_warehouse_name}?trusted_connection=yes&driver=ODBC+Driver+{odbc_version}+for+SQL+Server",
                           fast_executemany=True)
    try:
        engine_dwh.connect()
        print(f"Connected to {data_warehouse_name}")
    except InterfaceError:
        print(f"Unable to connect to {data_warehouse_name}")

    return engine_dwh


def read_tables(engine_dwh)->pd.DataFrame:
    # 1.fact_venta    
    fact_venta = pd.read_sql_table('FACT_VENTA', engine_dwh)  
    
    # 2.dim_vendedor
    dim_vendedor = pd.read_sql_table('DIM_VENDEDOR', engine_dwh)  

    return fact_venta,dim_vendedor


def incremental_load(source_path:str,fact_venta:pd.DataFrame,dim_vendedor:pd.DataFrame,engine_dwh,data_warehouse_name)->None: 
    path=source_path+'/*/*.txt'
    txt_paths = glob.glob(path)

    for txt_path in txt_paths:

        df=pd.read_csv(txt_path,header=None)

        df['cod_banco']=df[0].str[0:5]
        df['nombre_tipo_documento']=df[0].str[5:6]
        df['codigo_interno_1']=df[0].str[6:11]
        df['fecha_venta']=df[0].str[13:21]
        df['precio_unitario']=df[0].str[21:29]
        df['cantidad']=df[0].str[29:31]
        df['codigo_interno_2']=df[0].str[33:34]
        df['cod_documento']=df[0].str[34:44]
        df['codigo_interno_3']=df[0].str[43:45]
        df['dni_cliente']=df[0].str[48:56]
        df['codigo_interno_4']=df[0].str[56:58]
        df['cod_producto']=df[0].str[58:67]
        df['cod_vendedor']=df[0].str[67:74]
        df['codigo_interno_5']=df[0].str[74:76]
        
        #fecha_venta
        df['fecha_venta'] = pd.to_datetime(df['fecha_venta'], format='%Y%m%d')
        #precio_unitario y cantidad
        df = df.astype({"precio_unitario": np.float64, "cantidad": np.int64})
        #cod_documento 
        df['cod_documento'] = df['nombre_tipo_documento'] + df['cod_documento'].str[1:]
        #nombre_tipo_documento
        df['nombre_tipo_documento'] = df['nombre_tipo_documento'].apply(lambda x: "FACTURA" if x == "F" else "BOLETA")
        #cod_producto
        df['cod_producto'] = 'PROD'+ df['cod_producto'].str[4:]
        #cod_vendeddor
        df['cod_vendedor'] = 'VEND'+ df['cod_vendedor'].str[4:]
        #estado
        df['estado'] = 'VENDIDO'
            
        # 1.fact_venta
        df_join = df.merge(dim_vendedor,how='left', on='cod_vendedor')
        df_source_fv = df_join[['cod_documento','dni_cliente','vendedor','nombre_tipo_documento','estado','fecha_venta',
                         'cod_producto','precio_unitario','cantidad','cod_banco']]\
                         .set_index(['cod_documento','cod_producto'])
        
        df_source_fv=df_source_fv[~df_source_fv.index.isin(fact_venta.set_index(['cod_documento','cod_producto']).index)]\
                        .reset_index(level=[0,1])
        new_records_fv=df_source_fv.shape[0]

        if new_records_fv==0:
            print(f"From:  {txt_path[-11:]} file\n\t{new_records_fv} new records were added to {data_warehouse_name}.FACT_VENTA")
        else:
            fact_venta = pd.concat([fact_venta,df_source_fv],axis=0,ignore_index=True)
            df_source_fv.to_sql(name='FACT_VENTA', con=engine_dwh, if_exists='append',index=False)
            print(f"From:  {txt_path[-11:]} file\n\t{new_records_fv} new records were added to {data_warehouse_name}.FACT_VENTA")

    print("End of loading")    
                    

def main_flow(params):
        
    server_name = params.name
    data_warehouse_name = params.database
    source_path = params.path 
    odbc_version = params.driver 

    engine_dwh=connection(server_name,data_warehouse_name,odbc_version)
    fact_venta,dim_vendedor=read_tables(engine_dwh)
    incremental_load(source_path,fact_venta,dim_vendedor,engine_dwh,data_warehouse_name) 

if __name__ =='__main__':

    parser = argparse.ArgumentParser(description='ETL')

    parser.add_argument('--name', required=True, help='server name')
    parser.add_argument('--database', required=True, help='database name')
    parser.add_argument('--path', required=True, help='path')
    parser.add_argument('--driver', required=True, help='driver')

    args = parser.parse_args()

    main_flow(args)

