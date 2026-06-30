"""Tests for scripts/package_check.py."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SCRIPT_DIR))

from package_check import FAST_TEST_MODULES, unittest_command  # noqa: E402


class PackageCheckTests(unittest.TestCase):
    def test_default_unittest_command_uses_fast_subset(self):
        command = unittest_command(full=False)
        self.assertEqual(command[:3], [sys.executable, "-m", "unittest"])
        self.assertEqual(command[3:], FAST_TEST_MODULES)
        self.assertNotIn("discover", command)

    def test_full_unittest_command_uses_discover(self):
        command = unittest_command(full=True)
        self.assertEqual(
            command,
            [
                sys.executable,
                "-m",
                "unittest",
                "discover",
                "-s",
                "scripts/tests",
                "-p",
                "test_*.py",
            ],
        )


if __name__ == "__main__":
    unittest.main()
