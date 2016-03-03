#!/usr/bin/env python
# coding: utf-8

#########################################################################
#########################################################################

DESCRIPTION = """
"""

"""
Testes
Entrada 01:

I 5 6
L 2 3 A
S one.bmp
G 2 3 J
V 2 3 4 W
H 3 4 2 Z
F 3 3 J
S two.bmp
X

Saida 01:

one.bmp
OOOOO
OOOOO
OAOOO
OOOOO
OOOOO
OOOOO

two.bmp
JJJJJ
JJZZJ
JWJJJ
JWJJJ
JJJJJ
JJJJJ

Entrada 02:

I 10 9
L 5 3 A
G 2 3 J
V 2 3 4 W
H 1 10 5 Z
F 3 3 J
K 2 7 8 8 E
F 9 9 R
S one.bmp
X

Saida 02:

one.bmp
JJJJJJJJJJ
JJJJJJJJJJ
JWJJAJJJJJ
JWJJJJJJJJ
ZZZZZZZZZZ
RRRRRRRRRR
REEEEEEERR
REEEEEEERR
RRRRRRRRRR
"""

import unittest
from bitmap import BitMap


class TestBitMap(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        cls.v_str = [
            "I 5 6",
            "L 2 3 A",
            "S one.bmp",
            "G 2 3 J",
            "V 2 3 4 W",
            "H 3 4 2 Z",
            "F 3 3 J",
            "S two.bmp",
            "X"]

    @classmethod
    def tearDownClass(cls):
        pass

    def test_str(self):
        """ Test BitMap: create
        """
        for bitstr in self.v_str:
            bm = BitMap.fromstring(bitstr)
            self.assertEqual(self.helper_str_zfill(bitstr), bm.tostring())

    def test_count(self):
        for bitstr in self.v_str:
            bm = BitMap.fromstring(bitstr)
            self.assertEqual(bitstr.count("1"), bm.count())
            self.assertEqual(bitstr.count("1"),
                             len([i for i in xrange(bm.size()) if bm.test(i)]))

        for bitstr in self.v_str[:-4]:
            self.assertTrue(BitMap.fromstring(bitstr).any())
        self.assertTrue(BitMap.fromstring(self.v_str[-2]).all())
        self.assertTrue(BitMap.fromstring(self.v_str[-1]).none())

if __name__ == '__main__':
    unittest.main(failfast=True)
    # cProfile.run('unittest.main(failfast=True)')
