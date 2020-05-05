# coding=utf-8

import unittest
import BeautifulReport.BeautifulReport
import os
import yuanquanzhongzuihoushengxiadeshuzilcof

# testCase_path = "/Users/jielao/Desktop/PycharmProjects/Leetcode/"
testCase_path = "/Users/hello/git/mine_project/LeetCode_for_fun/LeetCode_for_fun"
# report_path = os.getcwd() + "/report/"
report_path = os.path.join(testCase_path, "report")
if not os.path.exists(report_path):
    os.mkdir(report_path)
fileName = report_path + "result_1.html"


class MyTestCase(unittest.TestCase):
    test_cases = [
        [5, 3, 3],
        [10, 17, 2]
    ]

    @BeautifulReport.BeautifulReport.add_test_img()
    def test_func(self):
        # self.assertEqual(True, False)
        s = yuanquanzhongzuihoushengxiadeshuzilcof.Solution()
        for test_case in self.test_cases:
            try:
                self.assertEqual(test_case[2], s.lastRemaining(test_case[0], test_case[1]))
            except AssertionError as e:
                print("Assert went wrong, content is %s" % e)
                raise e


if __name__ == '__main__':
    # unittest.main()
    # 创建套件
    # suite = unittest.TestSuite()

    # 创建加载器，并加载测试用例
    # loader = unittest.TestLoader()
    # loader = unittest.defaultTestLoader
    # suite.addTest(unittest.defaultTestLoader.discover(start_dir=testCase_path, pattern="test_*.py"))
    # suite.addTests(unittest.)

    test_suite = unittest.defaultTestLoader.discover(start_dir=testCase_path, pattern="test_*.py")

    # 生成测试报告
    runner = BeautifulReport.BeautifulReport(test_suite)
    runner.report(
        description="Beautiful report",
        filename=fileName,
        log_path=report_path
        # log_path=testReport_path
    )

    # 创建启动器
    # runner = unittest.TextTestRunner()
    # runner.run(suite)