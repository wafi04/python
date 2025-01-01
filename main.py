import psycopg2
from config   import config_db
from query.join import  left_join,inner_join

def main():
    conn = None
    try:
        conn = config_db()
        if conn is not None:
            conn.autocommit = True            
            left_join(conn)  
            inner_join(conn)  
    except (Exception, psycopg2.Error) as error:
        print("Error dalam proses", error)
    
    finally:
        if conn:
            conn.close()
            print("\nKoneksi PostgreSQL ditutup")

main()