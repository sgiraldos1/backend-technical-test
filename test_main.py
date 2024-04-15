import unittest

from tests.services.test_consulting_service import TestGetProperties


def main():
    suite=unittest.TestSuite()
    suite.addTest(TestGetProperties())

    unittest.main()



if __name__=="__name__":
    main()
