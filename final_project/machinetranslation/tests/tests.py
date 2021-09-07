'''
Tests for translator.py
'''

import unittest
from ibm_cloud_sdk_core.api_exception import ApiException

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    '''
    Test the englishToFrench method
    '''

    def test1(self):
        '''
        Test 1
        '''
        # test for null input
        with self.assertRaises(ApiException):
            english_to_french("")

        # test translation
        self.assertEqual(english_to_french("Hello"), "Bonjour")


class TestFrenchToEnglish(unittest.TestCase):
    '''
    Test the frenchToEnglish method
    '''

    def test1(self):
        '''
        Test 1
        '''
        # Test for null input
        with self.assertRaises(ApiException):
            french_to_english("")

        # Test translation
        self.assertEqual(french_to_english("Bonjour"), "Hello")

unittest.main()
