from query.format import execute_query
def left_join(conn):     
    query  =  """
        SELECT 
            k.id AS "Id",
            k.name AS "Nama Karyawan",
            k.salary AS "Gaji",
            d.name AS "Departement",
            p.title AS "Position"
        FROM 
            karyawan k
        LEFT JOIN 
            department  d ON k.department_id = d.id
        LEFT JOIN 
            position  p ON k.id = p.id
        """
    
    return execute_query(conn,query,"LEFT JOIN QUERY")

def inner_join(conn):     
    query = """
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
    
    return execute_query(conn,query,"INNER JOIN QUERY")
