import unittest

from src.models.ice_cream_stand import IceCreamStand


class TestIceCreamStand(unittest.TestCase):

    def test_flavors_available(self):
        #setup
        ice_cream = IceCreamStand("Andre Icecream", "Cakeshop", ["Morango", "Baunilha", "Chocolate Dark"])
        expected_result = "No momento temos os seguintes sabores de sorvete disponíveis: Morango, Baunilha, Chocolate Dark"
        #test
        flavors = ice_cream.flavors_available()
        #result
        self.assertEqual(expected_result, flavors)

    def test_flavors_not_available(self):
        #setup
        ice_cream = IceCreamStand("Andre Icecream", "Cakeshop", [])
        expected_result = "Estamos sem estoque atualmente!"
        #test
        flavors = ice_cream.flavors_available()
        #result
        self.assertEqual(expected_result, flavors)

    def test_find_flavor(self):
        # setup
        ice_cream = IceCreamStand("Andre Icecream", "Cakeshop", ["Morango", "Baunilha", "Chocolate Dark"])
        requested_flavor = "Chocolate Dark"
        expected_result = "Temos no momento Chocolate Dark!"
        # test
        flavor = ice_cream.find_flavor(requested_flavor)
        # result
        self.assertEqual(expected_result, flavor)

    def test_find_flavor_error(self):
        # setup
        ice_cream = IceCreamStand("Andre Icecream", "Cakeshop", ["Morango", "Baunilha", "Chocolate Dark"])
        requested_flavor = "Flocos"
        expected_result = "Não temos no momento Flocos!"
        # test
        flavor = ice_cream.find_flavor(requested_flavor)
        # result
        self.assertEqual(expected_result, flavor)

    def test_add_flavor(self):
        # setup
        ice_cream = IceCreamStand("Andre Icecream", "Cakeshop", ["Morango", "Baunilha", "Chocolate Dark"])
        flavor_add = "Flocos"
        expected_result = f"{flavor_add} adicionado ao estoque!"
        # test
        flavor = ice_cream.add_flavor(flavor_add)
        # result
        self.assertEqual(expected_result, flavor)

    def test_add_same_flavor(self):
        # setup
        ice_cream = IceCreamStand("Andre Icecream", "Cakeshop", ["Morango", "Baunilha", "Chocolate Dark"])
        flavor_add = "Morango"
        expected_result = "Sabor já disponivel!"
        # test
        flavor = ice_cream.add_flavor(flavor_add)
        # result
        self.assertEqual(expected_result, flavor)
