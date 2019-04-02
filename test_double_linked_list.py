from unittest import TestCase

from main.double_linked_list import DoubleLinkedList

class TestDoubleLinkedList(TestCase):

    def test_empty_list(self):
        doubly_linked_list = DoubleLinkedList()
        actual_str = str(doubly_linked_list)
        expected_str = ''
        self.assertEqual(expected_str, actual_str)


    def test_add(self):
        double_linked_list = DoubleLinkedList()
        double_linked_list.add_first(2)
        double_linked_list.add_first(3)
        expected_str = str(double_linked_list)
        self.assertEqual(expected_str,'32')
        expected_head= double_linked_list.head.value
        expected_tail= double_linked_list.tail.value
        self.assertEqual(expected_head,3)
        self.assertEqual(expected_tail, 2)

        double_linked_list.add_last(1)
        new_expected_str = str(double_linked_list)
        self.assertEqual(new_expected_str,'321')
        expected_head= double_linked_list.head.value
        expected_tail= double_linked_list.tail.value
        self.assertEqual(expected_head,3)
        self.assertEqual(expected_tail, 1)

        double_linked_list.remove_first()
        new_expected_str = str(double_linked_list)
        self.assertEqual(new_expected_str, '21')
        expected_head = double_linked_list.head.value
        expected_tail = double_linked_list.tail.value
        self.assertEqual(expected_head, 2)
        self.assertEqual(expected_tail, 1)

        double_linked_list.remove_last()
        new_expected_str = str(double_linked_list)
        self.assertEqual(new_expected_str, '2')
        expected_head = double_linked_list.head.value
        expected_tail = double_linked_list.tail.value
        self.assertEqual(expected_head, 2)
        self.assertEqual(expected_tail, 2)

        double_linked_list.remove_last()
        expected_str = str(double_linked_list)
        self.assertEqual(expected_str, '')

        self.assertRaises(Exception,double_linked_list.remove_last)

    def test_remove_at_nth_position(self):
        double_linked_list = DoubleLinkedList()
        double_linked_list.add_first(5)
        double_linked_list.add_first(4)
        double_linked_list.add_first(6)
        double_linked_list.add_first(3)
        double_linked_list.add_first(2)
        expected_str= str(double_linked_list)
        self.assertEqual(expected_str,'23645')
        expected_size = double_linked_list.size
        self.assertEqual(expected_size,5)
        value = str(double_linked_list.remove_at_nth_position(2))
        self.assertEqual(value,'6')
        expected_str = str(double_linked_list)
        self.assertEqual(expected_str,'2345')
        expected_size = double_linked_list.size
        self.assertEqual(expected_size,4)
        self.assertRaises(Exception,double_linked_list.remove_at_nth_position,7)
        value = str(double_linked_list.remove_at_nth_position(4))
        self.assertEqual(value, '5')










