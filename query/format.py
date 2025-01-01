from tabulate  import tabulate
import psycopg2
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