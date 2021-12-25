import unittest
from sqdb.conditionalquery import *

class TestForUser(unittest.TestCase):

    foruser = ForUser()
    foradmin = ForAdmin()

    def test_enteruserdata1(self):
        output = self.foruser.enteruserdata('helloe','testname','testcaste','9800010001','testpassword')
        self.assertIs(output,True)

    def test_enteruserdata2(self):
        output = self.foruser.enteruserdata('','jay','bad','1000000000','tpa')
        self.assertIs(output,False)

    def test_checkusername1(self):
        output = self.foruser.checkusername('neeschal00')
        self.assertIs(output,False)

    def test_checkusername2(self):
        output = self.foruser.checkusername('sunil')
        self.assertIs(output,False)

    def test_searchmovie(self):
        output = self.foruser.searchmovie('')
        self.assertFalse(output)

    def test_deletemovie(self):
        output = self.foradmin.deletemovie('Inception')
        self.assertTrue(output)

    def test_checkbooked(self):
        output = self.foradmin.checkbooked()
        self.assertTrue(output)

    def test_updateaddition(self):
        output = self.foradmin.updateaddition('Interstellar','Drama')
        self.assertIs(output, True)


if __name__ == '__main__':
    unittest.main()


























