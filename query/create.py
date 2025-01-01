import  psycopg2
def create_data(conn):
    try:
        csr = conn.cursor()
        csr.execute(
        """
            INSERT INTO position (title,grade_level,min_salary,max_salary) VALUES 
            ('spesialis',2,10000,30000);
        """
        )
        conn.commit()  
        return print("succcess")
    except (Exception, psycopg2.Error) as error:
        print(f"Error saat menjalankan", error)
        return None
