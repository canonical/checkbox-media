#!/usr/bin/env python3

import os
import unittest

import intel_gpu_top_parser

logfile1 = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    "data",
    "intel_gpu_top_h264_gst_encoding.log",
)
logfile2 = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    "data",
    "intel_gpu_top_no_gpu_usage.log",
)


class TestParseLog(unittest.TestCase):
    def test_parse_ok(self):
        avg = intel_gpu_top_parser.parse(logfile1)
        self.assertEqual(avg, 35.8689902)

    def test_parse_no_gpu(self):
        avg = intel_gpu_top_parser.parse(logfile2)
        self.assertEqual(avg, 0.0)

    def test_wrong_file(self):
        with self.assertRaises(FileNotFoundError):
            intel_gpu_top_parser.parse("wrong_log_file.log")
