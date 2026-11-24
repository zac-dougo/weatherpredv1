import unittest

import weatherpredv1


class PackageSmokeTest(unittest.TestCase):
    def test_version_is_non_empty(self) -> None:
        self.assertIsInstance(weatherpredv1.__version__, str)
        self.assertTrue(weatherpredv1.__version__)


if __name__ == "__main__":
    unittest.main()
