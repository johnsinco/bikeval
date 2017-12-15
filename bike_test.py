import unittest
import lxml
from bike import Bike

class BikeTest(unittest.TestCase):
    # test that the bike class works

    def test_title(self):
        fixture = lxml.html.fromstring(open('testbike.html').read())
        subj = Bike(fixture)
        subj.title == 'foo'


if __name__ == '__main__':
    unittest.main()
