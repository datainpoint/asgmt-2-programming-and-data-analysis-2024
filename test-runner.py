import unittest
import importlib

class TestAssignmentTwo(unittest.TestCase):
    def test_01_convert_integer_to_weekday(self):
        self.assertEqual(asgmt.convert_integer_to_weekday(0), 'Sunday')
        self.assertEqual(asgmt.convert_integer_to_weekday(1), 'Monday')
        self.assertEqual(asgmt.convert_integer_to_weekday(2), 'Tuesday')
        self.assertEqual(asgmt.convert_integer_to_weekday(3), 'Wednesday')
        self.assertEqual(asgmt.convert_integer_to_weekday(4), 'Thursday')
        self.assertEqual(asgmt.convert_integer_to_weekday(5), 'Friday')
        self.assertEqual(asgmt.convert_integer_to_weekday(6), 'Saturday')
    def test_02_convert_integer_to_weekday_and_abb(self):
        self.assertEqual(asgmt.convert_integer_to_weekday_and_abb(0), ('Sunday', 'Sun'))
        self.assertEqual(asgmt.convert_integer_to_weekday_and_abb(1), ('Monday', 'Mon'))
        self.assertEqual(asgmt.convert_integer_to_weekday_and_abb(2), ('Tuesday', 'Tue'))
        self.assertEqual(asgmt.convert_integer_to_weekday_and_abb(3), ('Wednesday', 'Wed'))
        self.assertEqual(asgmt.convert_integer_to_weekday_and_abb(4), ('Thursday', 'Thu'))
        self.assertEqual(asgmt.convert_integer_to_weekday_and_abb(5), ('Friday', 'Fri'))
        self.assertEqual(asgmt.convert_integer_to_weekday_and_abb(6), ('Saturday', 'Sat'))
    def test_03_sort_list_with_ascending_order(self):
        self.assertEqual(asgmt.sort_list_with_ascending_order([6, 6, 5, 5]),
                         [5, 5, 6, 6])
        self.assertEqual(asgmt.sort_list_with_ascending_order([3, 2, 1]),
                         [1, 2, 3])
        self.assertEqual(asgmt.sort_list_with_ascending_order([2, 5, 3]),
                         [2, 3, 5])
        self.assertEqual(asgmt.sort_list_with_ascending_order([2, 5, 3, 11, 7]),
                         [2, 3, 5, 7, 11])
        self.assertEqual(asgmt.sort_list_with_ascending_order([11, 7, 5, 3, 2]),
                         [2, 3, 5, 7, 11])
    def test_04_sort_list_with_descending_order(self):
        self.assertEqual(asgmt.sort_list_with_descending_order([5, 5, 6, 6]),
                         [6, 6, 5, 5])
        self.assertEqual(asgmt.sort_list_with_descending_order([1, 2, 3]),
                         [3, 2, 1])
        self.assertEqual(asgmt.sort_list_with_descending_order([2, 5, 3]),
                         [5, 3, 2])
        self.assertEqual(asgmt.sort_list_with_descending_order([2, 5, 3, 11, 7]),
                         [11, 7, 5, 3, 2])
        self.assertEqual(asgmt.sort_list_with_descending_order([2, 3, 5, 7, 11]),
                         [11, 7, 5, 3, 2])
    def test_05_retrieve_the_first_three_characters(self):
        self.assertEqual(asgmt.retrieve_the_first_three_characters("Python"), "Pyt")
        self.assertEqual(asgmt.retrieve_the_first_three_characters("Reticulate"), "Ret")
        self.assertEqual(asgmt.retrieve_the_first_three_characters("Anaconda"), "Ana")
        self.assertEqual(asgmt.retrieve_the_first_three_characters("Skywalker"), "Sky")
        self.assertEqual(asgmt.retrieve_the_first_three_characters("Anakin"), "Ana")
    def test_06_remove_the_first_and_last_element(self):
        self.assertEqual(asgmt.remove_the_first_and_last_element([2, 3, 5, 7, 11]), [3, 5, 7])
        self.assertEqual(asgmt.remove_the_first_and_last_element(["Python", "Reticulate", "Anaconda"]), ["Reticulate"])
        self.assertEqual(asgmt.remove_the_first_and_last_element([2, 3, 5]), [3])
        self.assertEqual(asgmt.remove_the_first_and_last_element(["Python", "Reticulate", "Anaconda"]), ["Reticulate"])
        self.assertEqual(asgmt.remove_the_first_and_last_element([2, 3, 5, 7, 11]), [3, 5, 7])
    def test_07_convert_weekday_to_integer(self):
        self.assertEqual(asgmt.convert_weekday_to_integer("Sunday"), 0)
        self.assertEqual(asgmt.convert_weekday_to_integer("Monday"), 1)
        self.assertEqual(asgmt.convert_weekday_to_integer("Tuesday"), 2)
        self.assertEqual(asgmt.convert_weekday_to_integer("Wednesday"), 3)
        self.assertEqual(asgmt.convert_weekday_to_integer("Thursday"), 4)
        self.assertEqual(asgmt.convert_weekday_to_integer("Friday"), 5)
        self.assertEqual(asgmt.convert_weekday_to_integer("Saturday"), 6)
    def test_08_find_taipei_city_zip_code(self):
        self.assertEqual(asgmt.find_taipei_city_zip_code("中正區"), 100)
        self.assertEqual(asgmt.find_taipei_city_zip_code("大同區"), 103)
        self.assertEqual(asgmt.find_taipei_city_zip_code("中山區"), 104)
        self.assertEqual(asgmt.find_taipei_city_zip_code("松山區"), 105)
        self.assertEqual(asgmt.find_taipei_city_zip_code("大安區"), 106)
        self.assertEqual(asgmt.find_taipei_city_zip_code("萬華區"), 108)
        self.assertEqual(asgmt.find_taipei_city_zip_code("信義區"), 110)
        self.assertEqual(asgmt.find_taipei_city_zip_code("士林區"), 111)
        self.assertEqual(asgmt.find_taipei_city_zip_code("北投區"), 112)
        self.assertEqual(asgmt.find_taipei_city_zip_code("內湖區"), 114)
        self.assertEqual(asgmt.find_taipei_city_zip_code("南港區"), 115)
        self.assertEqual(asgmt.find_taipei_city_zip_code("文山區"), 116)
    def test_09_sing_do_re_mi(self):
        self.assertEqual(asgmt.sing_do_re_mi("Do"), 'a deer, a female deer.')
        self.assertEqual(asgmt.sing_do_re_mi("Re"), 'a drop of golden sun.')
        self.assertEqual(asgmt.sing_do_re_mi("Mi"), 'a name I call myself.')
        self.assertEqual(asgmt.sing_do_re_mi("Fa"), 'a long long way to run.')
        self.assertEqual(asgmt.sing_do_re_mi("So"), 'a needle pulling thread.')
        self.assertEqual(asgmt.sing_do_re_mi("La"), 'a note to follow so.')
        self.assertEqual(asgmt.sing_do_re_mi("Ti"), 'a drink with jam and bread.')
    def test_10_remove_duplicates(self):
        self.assertEqual(asgmt.remove_duplicates([5, 5, 6, 6]), [5, 6])
        self.assertEqual(asgmt.remove_duplicates([2, 2, 6, 6]), [2, 6])
        self.assertEqual(asgmt.remove_duplicates([9, 9, 8, 1]), [1, 8, 9])
        self.assertEqual(asgmt.remove_duplicates([7, 7, 8, 8]), [7, 8])
        self.assertEqual(asgmt.remove_duplicates([2, 7, 7, 2]), [2, 7])

asgmt = importlib.import_module("asgmt")
suite = unittest.TestLoader().loadTestsFromTestCase(TestAssignmentTwo)
runner = unittest.TextTestRunner(verbosity=2)
test_results = runner.run(suite)
number_of_failures = len(test_results.failures)
number_of_errors = len(test_results.errors)
number_of_test_runs = test_results.testsRun
number_of_successes = number_of_test_runs - (number_of_failures + number_of_errors)
print("You've got {} successes among {} questions.".format(number_of_successes, number_of_test_runs))