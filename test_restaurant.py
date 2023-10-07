import unittest

from src.models.restaurant import Restaurant


class TestRestaurant(unittest.TestCase):

    def test_describe_restaurant(self):
        # setup
        restaurant = Restaurant("Andre", "Massas")
        expected_result = f"Esse restaturante chama Andre and serve Massas. " \
                          f"Esse restaturante está servindo 0 consumidores desde que está aberto."
        # test
        describre = restaurant.describe_restaurant()
        # result
        self.assertEqual(expected_result, describre)

    def test_open_restaurant(self):
        # setup
        restaurant = Restaurant("Andre", "Massas")
        expected_result1 = "Andre agora está aberto!"
        # test
        is_open_restaurant = restaurant.open_restaurant()
        # result
        self.assertTrue(is_open_restaurant) and self.assertEqual(is_open_restaurant, expected_result1)

    def test_already_open_restaurant(self):
        # setup
        restaurant = Restaurant("Andre", "Massas")
        restaurant.open = True
        expected_result1 = "Andre já está aberto!"
        # test
        open_restaurant = restaurant.open_restaurant()
        # result
        self.assertEqual(open_restaurant, expected_result1)

    def test_already_close_restaurant(self):
        # setup
        restaurant = Restaurant("Andre", "Massas")
        expected_result1 = "Andre já está fechado!"
        # test
        is_close_restaurant = restaurant.close_restaurant()
        # result
        self.assertEqual(is_close_restaurant, expected_result1)

    def test_close_restaurant(self):
        # setup
        restaurant = Restaurant("Andre", "Massas")
        restaurant.open = True
        expected_result1 = "Andre agora está fechado!"
        # test
        close_restaurant = restaurant.close_restaurant()
        # result
        self.assertTrue(close_restaurant) and self.assertEqual(close_restaurant, expected_result1)

    def test_set_number_served(self):
        # setup
        restaurant = Restaurant("Andre", "Massas")
        restaurant.open = True
        clients = 10
        expected_result = f"{clients} de pessoas atendidas por este restaurante até o momento"
        # test
        set_number = restaurant.set_number_served(clients)
        # result
        self.assertEqual(set_number, expected_result)

    def test_set_number_served_fail(self):
        # setup
        restaurant = Restaurant("Andre", "Massas")
        clients = 10
        expected_result = f"Andre está fechado!"
        # test
        set_number = restaurant.set_number_served(clients)
        # result
        self.assertEqual(set_number, expected_result)

    def test_increment_number_served(self):
        # setup
        restaurant = Restaurant("Andre", "Massas")
        restaurant.open = True
        restaurant.set_number_served(10)
        increment_client = 12
        expected_result = f"{restaurant.number_served + increment_client} de pessoas atendidas por este restaurante"
        # test
        set_number = restaurant.increment_number_served(increment_client)
        # result
        self.assertEqual(set_number, expected_result)

    def test_increment_number_served_fail(self):
        # setup
        restaurant = Restaurant("Andre", "Massas")
        restaurant.set_number_served(10)
        increment_client = 12
        expected_result = f"Andre está fechado!"
        # test
        set_number = restaurant.increment_number_served(increment_client)
        # result
        self.assertEqual(set_number, expected_result)

