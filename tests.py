import unittest, datetime
import numbers_tools, date_tools

class TestNumberToolsTemplate(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        pass

    def test_percentage(self):
        pass

    def test_int_to_str(self):
        self.assertEqual(numbers_tools.stringuify_number(100), "100")
        self.assertEqual(numbers_tools.stringuify_number(1000), "1K")
        self.assertEqual(numbers_tools.stringuify_number(1100), "1.1K")
        self.assertEqual(numbers_tools.stringuify_number(1010), "1K")
        self.assertEqual(numbers_tools.stringuify_number(10000), "10K")
        self.assertEqual(numbers_tools.stringuify_number(100000), "100K")
        self.assertEqual(numbers_tools.stringuify_number(1000000), "1M")
        self.assertEqual(numbers_tools.stringuify_number(1100000), "1.1M")
        self.assertEqual(numbers_tools.stringuify_number(1010000), "1M")
        self.assertEqual(numbers_tools.stringuify_number(1001000), "1M")
        self.assertEqual(numbers_tools.stringuify_number(1000100), "1M")
        self.assertEqual(numbers_tools.stringuify_number(5460157), "5.5M")
        self.assertEqual(numbers_tools.stringuify_number(1047343),"1M")
        self.assertEqual(numbers_tools.stringuify_number(181568),"181.6K")
        self.assertEqual(numbers_tools.stringuify_number(12361234),"12.4M")
        self.assertEqual(numbers_tools.stringuify_number(12350001),"12.4M")
        self.assertEqual(numbers_tools.stringuify_number(12340000),"12.3M")
        self.assertEqual(numbers_tools.stringuify_number(2390),"2.4K")
        self.assertEqual(numbers_tools.stringuify_number(2300),"2.3K")
        self.assertEqual(numbers_tools.stringuify_number(2349),"2.3K")
        self.assertEqual(numbers_tools.stringuify_number(2351),"2.4K")

class TestDateToolsTemplate(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        pass

    def test_get_list_of_days(self):
        d1_7 = datetime.date(2016, 7, 1)
        d2_7 = datetime.date(2016, 7, 2)
        d2_6 = datetime.date(2016, 6, 2)

        self.assertEqual(date_tools.get_list_of_days(d2_7, d2_7, 1), [datetime.date(2016, 7, 2)])
        self.assertEqual(date_tools.get_list_of_days(d2_7, d1_7, 2), [datetime.date(2016, 7, 1), datetime.date(2016, 7, 2)])
        self.assertEqual(date_tools.get_list_of_days(d2_7, d2_6, 100), [datetime.date(2016, 6, 2), datetime.date(2016, 6, 3),
                                                           datetime.date(2016, 6, 4), datetime.date(2016, 6, 5),
                                                           datetime.date(2016, 6, 6), datetime.date(2016, 6, 7),
                                                           datetime.date(2016, 6, 8), datetime.date(2016, 6, 9),
                                                           datetime.date(2016, 6, 10), datetime.date(2016, 6, 11),
                                                           datetime.date(2016, 6, 12), datetime.date(2016, 6, 13),
                                                           datetime.date(2016, 6, 14), datetime.date(2016, 6, 15),
                                                           datetime.date(2016, 6, 16), datetime.date(2016, 6, 17),
                                                           datetime.date(2016, 6, 18), datetime.date(2016, 6, 19),
                                                           datetime.date(2016, 6, 20), datetime.date(2016, 6, 21),
                                                           datetime.date(2016, 6, 22), datetime.date(2016, 6, 23),
                                                           datetime.date(2016, 6, 24), datetime.date(2016, 6, 25),
                                                           datetime.date(2016, 6, 26), datetime.date(2016, 6, 27),
                                                           datetime.date(2016, 6, 28), datetime.date(2016, 6, 29),
                                                           datetime.date(2016, 6, 30), datetime.date(2016, 7, 1),
                                                           datetime.date(2016, 7, 2)])
        self.assertEqual(date_tools.get_list_of_days(d2_7, d2_6, 1), [datetime.date(2016, 7, 2)])
        self.assertEqual(date_tools.get_list_of_days(d2_7, d2_6, 0), [])

    def test_get_days_of_week_within_month(self):
        self.assertEqual(date_tools.get_days_of_week_within_month(2016,8,35), [datetime.date(2016, 8, 29),
                                                                               datetime.date(2016, 8, 30),
                                                                               datetime.date(2016, 8, 31)])
        self.assertEqual(date_tools.get_days_of_week_within_month(2016, 9, 35), [datetime.date(2016, 9, 1),
                                                                                 datetime.date(2016, 9, 2),
                                                                                 datetime.date(2016, 9, 3),
                                                                                 datetime.date(2016, 9, 4)])
        self.assertEqual(date_tools.get_days_of_week_within_month(2015, 12, 53), [datetime.date(2015, 12, 28),
                                                                                 datetime.date(2015, 12, 29),
                                                                                 datetime.date(2015, 12, 30),
                                                                                 datetime.date(2015, 12,31)])
        self.assertEqual(date_tools.get_days_of_week_within_month(2016, 1, 53), [datetime.date(2016, 1, 1),
                                                                                 datetime.date(2016, 1, 2),
                                                                                 datetime.date(2016, 1, 3)])


    def test_months_fy(self):
        self.assertEqual(date_tools.get_fy_months("fy16"),
                         ['April 16', 'May 16', 'June 16',
                            'July 16', 'August 16', 'September 16',
                            'October 16', 'November 16', 'December 16',
                            'January 16', 'February 16', 'March 16'])

        self.assertEqual(date_tools.get_fy_months("fy15"),
                         ['April 15', 'May 15', 'June 15',
                          'July 15', 'August 15', 'September 15',
                          'October 15','November 15','December 15',
                          'January 15', 'February 15', 'March 15'])




if __name__ == '__main__':
    unittest.main()