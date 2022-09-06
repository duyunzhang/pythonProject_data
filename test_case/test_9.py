"""
@file :  test_9.py
@author : 张福卫
@date : 2022/08/25 14:26
"""
import unittest


class TestDemo(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test1one(self):
        self.assertEqual(1, 1)

    # 实现的很简单。直接就跳过了
    @unittest.skip("直接跳过")
    def test2two(self):
        self.assertEqual(1, 1)

    # 判断跳过
    @unittest.skipIf(1 == 1, "条件1=1符合，跳过")
    def test3two(self):
        self.assertEqual(1, 1)

    @unittest.skipUnless(2 == 2, '条件为false,跳过')
    def test4two(self):
        self.assertEqual(1, 1)

if __name__ == "__main__":
    unittest.main()
