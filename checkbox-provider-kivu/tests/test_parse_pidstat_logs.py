#!/usr/bin/env python3

import os
import unittest

import parse_pidstat_logs

logfile1 = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    "data",
    "chromium_h264_video_vaapi_disabled_pidstat.log",
)
logfile2 = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    "data",
    "chromium_h264_video_vaapi_enabled_pidstat.log",
)


class TestParseLog(unittest.TestCase):
    def test_parse_ok(self):
        cpu_usage = parse_pidstat_logs.parse(logfile1)
        self.assertEqual(cpu_usage, 63.53)

    def test_wrong_file(self):
        with self.assertRaises(FileNotFoundError):
            parse_pidstat_logs.parse("wrong_log_file.log")
