import psycopg2

def config_db():
    conn = None
    try:
        conn = psycopg2.connect(**{
            'host': '',
            'database': '',
            'user': '',
            'password': '',
            'port': '' 
        })
        print("Connection Success")
        return conn
    except (Exception, psycopg2.Error) as error:
        print("Error saat koneksi ke PostgreSQL", error)
        return None
