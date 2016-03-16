import unittest
import GitApi
import json
import urllib2

class YourTest(unittest.TestCase):

    def test_language_count_two(self):
        data = [{'language':'Java'}, {'language':'C'}]
        self.assertEqual({'Java':1, 'C':1}, GitApi.language_count(data))

    def test_language_count_empty(self):
        data = []
        self.assertEqual({}, GitApi.language_count(data))

    def testGoodRequest(self):
        response = urllib2.urlopen("https://api.github.com/users/vasinwr/repos")
        data = json.load(response)
        self.assertGreaterEqual(len(GitApi.language_count(data)),0)

    def testRequestFail(self):
        badurl = "https://api.github.com/users/thisuserdoesnotexist/repos"
        with self.assertRaises(urllib2.HTTPError):
            GitApi.get_data(badurl)

unittest.main()
