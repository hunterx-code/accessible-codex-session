#!/usr/bin/env python3
"""Tests for sr_text_filter.py."""

from __future__ import annotations

import unittest

import sr_text_filter


class ScreenReaderTextFilterTests(unittest.TestCase):
    def test_filters_ansi_spinners_progress_and_repeats(self) -> None:
        noisy = "\x1b[32mRunning tests...\x1b[0m\n|\n/\n50%\n50%\n" + (
            "AssertionError: expected value\n" * 4
        )

        filtered = sr_text_filter.filter_text(noisy, max_repeats=2)

        self.assertIn("Running tests...", filtered)
        self.assertIn("AssertionError: expected value", filtered)
        self.assertNotIn("\x1b[32m", filtered)
        self.assertNotIn("\n|\n", filtered)
        self.assertNotIn("\n50%\n", filtered)
        self.assertEqual(filtered.count("AssertionError: expected value"), 2)
        self.assertIn("screen-reader filter removed", filtered)

    def test_preserves_meaningful_file_paths_and_test_names(self) -> None:
        noisy = "tests/test_example.py::test_failure FAILED\nsrc/app.py:12: error\n"

        filtered = sr_text_filter.filter_text(noisy)

        self.assertIn("tests/test_example.py::test_failure FAILED", filtered)
        self.assertIn("src/app.py:12: error", filtered)


if __name__ == "__main__":
    unittest.main()
