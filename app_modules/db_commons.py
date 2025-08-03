#
# Common database capabilities
#
from peewee import PostgresqlDatabase, Model


app_db = PostgresqlDatabase(
        'testdb',
        user='test_user',
        password='simplepw'
    )

field_map = {
    "AUTO":"SERIAL",
    "BIGAUTO":"BIGSERIAL",
    "INTEGER":"INTEGER",
    "BIGINTEGER":"BIGINT",
    "SMALLINTEGER":"SMALLINT",
    "IDENTITY":"INT",
    "FLOAT":"REAL",
    "DOUBLE":"DOUBLE PRECISION",
    "DECIMAL":"NUMERIC",
    "CHAR":"VARCHAR",
    "VARCHAR":"VARCHAR",
    "FIXEDCHAR":"CHAR",
    "TEXT":"TEXT",
    "BLOB":"BYTEA",
    "BIT":"BIGINT",
    "BIGBIT":"BYTEA",
    "UUID":"UUID",
    "BINARYUUID":"BYTEA",
    "DATETIME":"TIMESTAMP",
    "DATE":"DATE",
    "TIME":"TIME",
    "TIMESTAMP":"INTEGER",
    "IP":"BIGINT",
    "BOOLEAN":"BOOLEAN",
    "FOREIGNKEY":"INTEGER",
}


class BaseAppObject (Model):
    '''
        Extension of the base peewee model to standardise the database attribute and include a 
        DEB synchroniser function
    '''

    class Meta:
        database = app_db

    @classmethod
    def sync_model(cls):
        '''
            Synchronise current class definition with DB schema.
            Any missing attributes will be assumed to ne new columns (not renamed)
            and will be created as NULLABLE.
        '''
        l_table_name = cls._meta.table_name
        l_db = cls._meta.database
        print(f"Check DB schema for {cls.__name__} in database = {l_db.database}")
        # If the table doesn't exist, create it.
        tbl_list = l_db.get_tables()
        if l_table_name not in tbl_list:
            # If the table doesn't exist create it
            print(f"Creating table = {l_table_name}")
            cls.create_table()
        else:
            # If the table does exist
            # Look for missing columns and add them
            print(f"Checking existing schema for table {l_table_name}")
            l_obj_columns = cls._meta.fields
            l_db_columns = l_db.get_columns(l_table_name)
            l_db_col_names = []
            for col_def in l_db_columns:
                l_db_col_names.append(col_def.name)
            for oc in l_obj_columns:
                if oc not in l_db_col_names:
                    # Add Missingcolumn to table
                    l_fld_type = l_obj_columns[oc].field_type
                    print(f"Create column {oc} Structure {l_fld_type}")
                    l_ddl = f"ALTER TABLE public.{l_table_name} ADD COLUMN {oc} {field_map[l_fld_type]}"
                    if l_fld_type in ["CHAR","FIXEDCHAR","VARCHAR"]:
                        l_ddl += f"({l_obj_columns[oc].max_length});"
                    else:
                        l_ddl += ";"
                    l_db.execute_sql(l_ddl)
        print(f"Done - {cls.__name__} synchronised with table {l_table_name}\n")

'''
    An alternative approach would be to look for differences in the peewee object
    If they are different, rename the old table, create the new version of the table, 
    then copy the data back across and drop the old table.

    Care would need to be taken with default values, renamed columns etc.

'''
        
