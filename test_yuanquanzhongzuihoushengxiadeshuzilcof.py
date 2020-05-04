import unittest
import Leetcode
from exceptions import AssertionError

global testCase_path = "/Users/jielao/Desktop/PycharmProjects/Leetcode"

class MyTestCase(unittest.TestCase):
    test_cases = [
        [5, 3, 3],
        [10, 17, 2]
    ]

    def tearDown(self, index):
        print "Now!!The num %d testcase has been tested!!" % index

    def test_func(self):
        # self.assertEqual(True, False)
        s = Leetcode.yuanquanzhongzuihoushengxiadeshuzilcof.Solution()
        for test_case in self.test_cases:
            try:
                self.assertEqual(test_case[2], s.lastRemaining(test_case[0], test_case[1]))
            except AssertionError as e:
                print "Assert went wrong, content is %s" % e
                raise e
            finally:
                self.tearDown(self.test_cases.index(test_case))


if __name__ == '__main__':
    # unittest.main()
    # 创建套件
    suite = unittest.TestSuite()

    # 创建加载器，并加载测试用例
    # loader = unittest.TestLoader()
    loader = unittest.defaultTestLoader()
    suite.addTest(loader.discover(start_dir=testCase_path, pattern="test_*.py"))

    # 创建启动器
    runner = unittest.TextTestRunner()
    runner.