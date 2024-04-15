import unittest
from unittest.mock import MagicMock, patch
from src.services.consulting_service import get_properties

class TestGetProperties(unittest.TestCase):

    def test_get_properties_with_filters(self):
        # Simulating a connection to the database and a cursor
        cursor_mock = MagicMock()
        connection_mock = MagicMock()
        connection_mock.cursor.return_value = cursor_mock

        with patch('src.services.consulting_service.db_connection', return_value=connection_mock):
            # data in 
            year = 2022
            city = 'Medellin'
            status = 'en_venta'

            #  consulting data 
            expected_result = [{'id': 1, 'address': '123 Main St', 'city': 'medellin', 'price': 200000, 'year': 2022, 'description': 'Beautiful house', 'status': 'en_venta'}]
            cursor_mock.fetchall.return_value = expected_result

           #start function
            result = get_properties(year, city, status)

            # Checking that the SQL query was called with the correct filters
            cursor_mock.execute.assert_called_once_with(
                """
                SELECT  
                    DISTINCT(p.id) as id,
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
                WHERE s.name IN ('pre_venta', 'en_venta','vendido')
                AND s.name = %(status)s
                AND LOWER(p.city) = %(city)s
                AND p.year = %(year)s
                """,
                {'status': status, 'city': city.lower(), 'year': year}
            )

            # Checking that the expected result was returned
            self.assertEqual(result, expected_result)

   

