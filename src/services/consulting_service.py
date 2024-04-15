import json

from src.config.database import db_connection


def get_properties(year, city, status):
    conn = db_connection()
    cursor = conn.cursor()

    # SQL query using filters
    query = """
        SELECT  
            p.id,
            p.address,
            p.city,
            p.price,
            p.year,
            p.description,
            s.name As status
        FROM habi_db.status_history AS sh
        INNER JOIN (
            SELECT property_id, MAX(update_date) AS update_date
            FROM habi_db.status_history
            GROUP BY property_id
        ) AS latest_sh ON latest_sh.property_id = sh.property_id AND latest_sh.update_date = sh.update_date
        INNER JOIN habi_db.property AS p ON p.id = sh.property_id
        INNER JOIN habi_db.status AS s ON s.id = sh.status_id
        WHERE s.name  IN ('pre_venta', 'en_venta','vendido')
    """
    if status: 
        query = query + "AND s.name  = %(status)s"
    if city:
        query = query + "AND p.city  = %(city)s"    
    if year:
        query = query + "AND p.year  = %(year)s"


    filters = {"status": status, "city": city, "year": year}
    cursor.execute(query, filters)

    # Mapping the results to objects of the real estate class

    rows= cursor.fetchall()
    columns = [column[0] for column in cursor.description]

    properties = [dict(zip(columns,row))for row in rows]


    conn.close()
    return properties
