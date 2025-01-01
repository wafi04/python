import psycopg2
def update_data(conn):
    try:
        csr = conn.cursor()
        csr.execute(
        """
            UPDATE karyawan
            SET salary = 10000
        """
        )
        conn.commit()  
        return print("succcess")
    
    except (Exception, psycopg2.Error) as error:
        print(f"Error saat menjalankan", error)
        return None