from unittest import TestCase

from main import DoubleLinkedList


class TestDoubleLinkedList(TestCase):

    def test_empty_list(self):
        doubly_linked_list = DoubleLinkedList()
        expected_str = str(doubly_linked_list)
        actual_str = ''
        self.assertEqual(self, expected_str, actual_str)


    def test_add_first(self):
        double_linked_list = DoubleLinkedList()
        double_linked_list.add_first(self,2)
        expected_str = str(double_linked_list)
        self.assertEqual(self, expected_str,'3')
