import json

from src.config.database import db_connection


def get_properties(year, city, status):
    conn = db_connection()
    cursor = conn.cursor()

    # SQL query using filters
    query = """
        SELECT  id, address,city,price,year,description, status
        FROM property
        WHERE status = %(status)s
        AND city = %(city)s
        AND year = %(year)s
    """

    filters = {"status": status, "city": city, "year": year}
    cursor.execute(query, filters)

    # Mapping the results to objects of the real estate class

    property = [get_properties(*row) for row in cursor]

    conn.close()
    return property
