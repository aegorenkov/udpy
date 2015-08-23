from unittest import TestCase

from udpy.select import select


class TestSelect(TestCase):

    def test_new_case(self):
        select("Not a proper file")
