import unittest
from client3 import getDataPoint
from client3 import getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
       self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2))
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2))

  """ ------------ Add more unit tests ------------ """
  def test_getRatio(self):
    # Test case 1: price_a = 10, price_b = 5
    price_a = 10
    price_b = 5
    expected_ratio = 2.0
    self.assertEqual(getRatio(price_a, price_b), expected_ratio)

    # Test case 2: price_a = 0, price_b = 10
    price_a = 0
    price_b = 10
    expected_ratio = 0.0
    self.assertEqual(getRatio(price_a, price_b), expected_ratio)

    # Test case 3: price_a = 8, price_b = 0
    price_a = 8
    price_b = 0
    expected_ratio = None
    self.assertEqual(getRatio(price_a, price_b), expected_ratio)

    # Test case 4: price_a = 0, price_b = 0
    price_a = 0
    price_b = 0
    expected_ratio = None
    self.assertEqual(getRatio(price_a, price_b), expected_ratio)
     


if __name__ == '__main__':
    unittest.main()
