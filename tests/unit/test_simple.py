import unittest
from NyaaSort.NyaaSort import NyaaSort
import tests.utils
import os
import shutil


class TestSimple(unittest.TestCase):

    def setUp(self):
        base_dir = os.path.dirname(os.path.realpath(__file__))
        self.dir = tests.utils.copy_tree(base_dir)
        self.app = NyaaSort

    def test_init(self):
        self.assertEqual(self.app(self.dir, 'False').weak_error, False)
        self.assertEqual(self.app(self.dir, 'True').weak_error, False)
        self.assertEqual(self.app(self.dir).weak_error, False)
        self.assertEqual(self.app(self.dir, 0).weak_error, False)
        self.assertEqual(self.app(self.dir, 0).weak_error, False)
        self.assertEqual(self.app(self.dir, 'random').dir_path, self.dir)
        self.assertEqual(self.app(self.dir).dir_path, self.dir)
        self.assertEqual(self.app(self.dir, 'True').dir_path, self.dir)
        self.assertEqual(self.app(self.dir, 'False').dir_path, self.dir)
        self.assertEqual(self.app(self.dir, 'random').dir_path, self.dir)

    def test_anime_dict(self):
        folders = ['[DameDesuYo] Shingeki no Kyojin (The Final Season)',
                   '[Erai-raws] Enen no Shouboutai - Ni no Shou',
                   '[Multiple groups] Enen no Shouboutai S2']
        folders_dict = {'Enen no Shouboutai - Ni no Shou': '[Erai-raws] Enen no Shouboutai - Ni no Shou',
                        'Enen no Shouboutai S2': '[Multiple groups] Enen no Shouboutai S2',
                        'Shingeki no Kyojin (The Final Season)': '[DameDesuYo] Shingeki no Kyojin (The Final Season)'}
        # Test if no folders
        self.assertEqual(self.app(self.dir, 'False').get_anime_dict(['']), {})
        self.assertEqual(self.app(self.dir, 'True').get_anime_dict(['']), {})
        self.assertEqual(self.app(self.dir).get_anime_dict(['']), {})
        self.assertEqual(self.app(self.dir, 0).get_anime_dict(['']), {})
        self.assertEqual(self.app(self.dir, 'random').get_anime_dict(['']), {})
        self.assertEqual(self.app(self.dir, 'True').get_anime_dict(folders), folders_dict)
        self.assertEqual(self.app(self.dir, 'False').get_anime_dict(folders), folders_dict)
        self.assertEqual(self.app(self.dir).get_anime_dict(folders), folders_dict)
        self.assertEqual(self.app(self.dir, 0).get_anime_dict(folders), folders_dict)

    def test_move_anime(self):
        self.assertEqual(self.app(self.dir).move_anime(), '')

    def tearDown(self):
        # Remove the test dir
        shutil.rmtree(self.dir)


if __name__ == '__main__':
    unittest.main()
