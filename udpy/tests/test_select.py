from unittest import TestCase

import udpy
import os

DIRECTORY = os.getcwd()
SEP = os.sep

class TestSelect(TestCase):

    def test_select_sepal_length_should_match_dplyr(self):
        test_file_path = [DIRECTORY, 'udpy', 'tests', 'data',
                          'iris_select_sepal_length.csv']
        test_file_path = SEP.join(test_file_path)

        with open(test_file_path) as test_file:
            test_lines = [line for line in test_file.readlines()]

        file_path = [DIRECTORY, 'udpy', 'tests', 'data', 'iris_test.csv']
        file_path = SEP.join(file_path)

        lines = udpy.select(file_path, 'sepal_length')
        self.assertEqual(lines, test_file)