import os
import unittest
import subprocess
import json

_APP_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
_JLTO_FILEPATH = os.path.join(_APP_PATH, 'jlto', 'resources', 'scripts', 'jlto')


class TestJltoCommand(unittest.TestCase):
    def test__basic(self):
        listcontent = """\
aa bb cc
dd ee ff
"""

        cmd = [_JLTO_FILEPATH]
        p = subprocess.Popen(
                cmd,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT)

        actualRaw, _ = p.communicate(input=listcontent)
        actual = json.loads(actualRaw)

        expected = {
            'aa': 'bb cc',
            'dd': 'ee ff',
        }

        self.assertEquals(actual, expected)
