from insert_table import insert_sample_data, view_data, view_all_tables
from table_create import create_connection, create_tables




if __name__ == "__main__":
    conn = create_connection()
    create_tables(conn)
    insert_sample_data(conn)
#    view_data(conn)
    view_all_tables(conn)
    conn.close()
    print(" Database setup completed!")
else:
    print("Error")
