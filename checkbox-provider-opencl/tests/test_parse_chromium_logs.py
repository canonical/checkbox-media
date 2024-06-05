#!/usr/bin/env python3

import os
import unittest

import parse_chromium_logs

logfile1 = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    "data",
    "chromium_h264_video_vaapi_disabled.log",
)
logfile2 = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    "data",
    "chromium_h264_video_vaapi_enabled.log",
)


class TestParseLog(unittest.TestCase):
    def test_parse_ok(self):
        decoder = parse_chromium_logs.parse(logfile2)
        self.assertEqual(decoder, "VDAVideoDecoder")

    def test_is_hw_decoder(self):
        decoder = "VDAVideoDecoder"
        self.assertTrue(parse_chromium_logs.is_hw_decoder(decoder))

    def test_wrong_file(self):
        with self.assertRaises(FileNotFoundError):
            parse_chromium_logs.parse("wrong_log_file.log")
