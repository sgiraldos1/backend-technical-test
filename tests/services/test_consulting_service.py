import unittest
from unittest.mock import Mock, patch
from src.services.consulting_service import get_properties


class TestGetProperties(unittest.TestCase):

    @patch("src.services.consulting_service.db_connection")

    def test_get_properties_with_filters(self,mock_conn):

        # Simulating a connection to the database and a cursor
        
        mock_cursor= Mock()
        mock_conn.return_value.cursor.return_value = mock_cursor

        
            # data in 
        year = 2022
        city = 'Medellin'
        status = 'en_venta'

        mock_cursor.description=[

            ("id",str),
            ("address",str),
            ("city",str),
            ("price",float),
            ("year",int),
            ("description",str),
            ("status",str),
        ]

        #  consulting data 

        mock_cursor.fetchall.return_value=[(1,  '123 Main St', 'medellin', 200000,  2011,  'Beautiful house', 'en_venta')]


        
        expected_result = [{"id":1,"address" : '123 Main St',"city" :'medellin',"price": 200000,"year":  2011,"description" : 'Beautiful house', "status":'en_venta',}]
        

        #start function
        result = get_properties(year, city, status)


        # Checking that the expected result was returned
        self.assertEqual(result, expected_result)



