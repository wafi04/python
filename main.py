from tabulate import tabulate  
import psycopg2
from config   import config_db

def execute_query(conn, query, query_type):
    try:
        csr = conn.cursor()
        csr.execute(query)    
        columns = [desc[0] for desc in csr.description]
        
        rows = csr.fetchall()
        print(f"\n{'='*50}")
        print(f"{query_type} RESULT")
        print('='*50)
        
        print(tabulate(rows, headers=columns, tablefmt="grid"))
        
        return rows
    
    except (Exception, psycopg2.Error) as error:
        print(f"Error saat menjalankan {query_type}", error)
        return None

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

def main():
    conn = None
    try:
        conn = config_db()
        if conn is not None:
            conn.autocommit = True            
            left_join_query = """
            SELECT 
                k.id AS "Id",
                k.name AS "Nama Karyawan",
                k.salary AS "Gaji",
                d.name AS "Departement",
                p.title AS "Position"
            FROM 
                karyawan k
            INNER JOIN 
                department d ON k.department_id = d.id
            INNER JOIN 
                position p ON d.id = p.id
            ORDER BY 
                k.id;
            """
            execute_query(conn,left_join_query,"LEFT JOIN QUERY")
    
    except (Exception, psycopg2.Error) as error:
        print("Error dalam proses", error)
    
    finally:
        if conn:
            conn.close()
            print("\nKoneksi PostgreSQL ditutup")

main()