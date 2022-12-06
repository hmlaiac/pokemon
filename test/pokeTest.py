import unittest
from lib.pokeStudy import Crawler
import os
class TestPokeCrawler(unittest.TestCase):
    def test_info_crawler(self):
        link = "https://wiki.52poke.com/zh/%E5%AE%9D%E5%8F%AF%E6%A2%A6%E5%88%97%E8%A1%A8%EF%BC%88%E6%8C%89%E5%B8%95%E5%BA%95%E4%BA%9A%E5%9B%BE%E9%89%B4%E7%BC%96%E5%8F%B7%EF%BC%89"
        crawler = Crawler()
        df = crawler.download_9th_pokemon(link)
        self.assertEqual(400, len(df))

    def test_info_save(self):
        self.assertTrue(os.path.exists("..\\data\\poke9gen.csv"))

