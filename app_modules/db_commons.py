#
# Common database capabilities
#
from peewee import PostgresqlDatabase, Model


app_db = PostgresqlDatabase(
        'testdb',
        user='test_user',
        password='simplepw'
    )


class BaseAppObject (Model):

    class Meta:
        database = app_db

    @classmethod
    def sync_model(cls):
        l_table_name = cls._meta.table_name
        l_db = cls._meta.database
        print(f"Synchronise table {cls._meta.table_name} in DB = {db.database}")
        # If the table doesn't exist, create it.
        tbl_list = db.get_tables()
        if cls._meta.table_name not in tbl_list:
            # If the table doesn't exist create it
            print(f"Creating Table")
            cls.create_table()
        else:
            # If the table does exist
            # Look for missing columns and add them
            print("Checking table schema")
            l_obj_columns = ??
            l_db_columns = ??
            for oc in l_obj_columns:
                if oc not in l_db_columns:
                    #add attribute to table
