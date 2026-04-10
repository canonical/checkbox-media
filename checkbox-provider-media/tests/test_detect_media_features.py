#!/usr/bin/env python3
"""Non-regression tests for checkbox-provider-media/bin/detect-media-features."""

import importlib.util
import json
import tempfile
import unittest
from importlib.machinery import SourceFileLoader
from pathlib import Path


def _load_module():
    script_path = Path(__file__).resolve().parents[1] / "bin" / "detect-media-features"
    loader = SourceFileLoader("detect_media_features", str(script_path))
    spec = importlib.util.spec_from_loader("detect_media_features", loader)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load module from {script_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


mod = _load_module()


class TestDetectMediaFeatures(unittest.TestCase):
    def test_normalize_pci_id_is_lowercase_prefixed_and_trimmed(self):
        self.assertEqual(mod.normalize_pci_id("  8086  \n"), "0x8086")
        self.assertEqual(mod.normalize_pci_id("0X9A49"), "0x9a49")

    def test_load_media_db_builds_maps_and_defaults_vendor_id(self):
        payload = {
            "gpu_database": {
                "platforms": [
                    {
                        "name": "Intel GPU",
                        "architecture": "GenX",
                        "codename": "Foo",
                        "release_year": 2024,
                        "pci_ids": ["9A49"],
                        "media_feature": "MTL",
                    }
                ],
                "media_features": [
                    {
                        "name": "MTL",
                        "codecs": {
                            "decoders": [{"name": "h264", "max_resolution": "4k"}],
                            "encoders": [],
                        },
                    }
                ],
            }
        }

        with tempfile.TemporaryDirectory() as tmp:
            db = Path(tmp) / "media_features.json"
            db.write_text(json.dumps(payload), encoding="utf-8")

            pci_map, feature_map = mod.load_media_db(db)

        key = ("0x8086", "0x9a49")
        self.assertIn(key, pci_map)
        self.assertEqual(pci_map[key][0]["name"], "Intel GPU")
        self.assertIn("MTL", feature_map)

    def test_iter_pci_devices_filters_by_vendor_and_skips_broken_entries(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)

            dev_ok = root / "0000:00:02.0"
            dev_ok.mkdir()
            (dev_ok / "vendor").write_text("0x8086\n", encoding="utf-8")
            (dev_ok / "device").write_text("0x9A49\n", encoding="utf-8")

            dev_other = root / "0000:01:00.0"
            dev_other.mkdir()
            (dev_other / "vendor").write_text("0x1002\n", encoding="utf-8")
            (dev_other / "device").write_text("0x164E\n", encoding="utf-8")

            dev_broken = root / "0000:02:00.0"
            dev_broken.mkdir()
            (dev_broken / "vendor").write_text("0x8086\n", encoding="utf-8")
            # Missing device file should make this entry be skipped.

            devices = list(mod.iter_pci_devices(root, vendor_filter="8086"))

        self.assertEqual(len(devices), 1)
        self.assertEqual(devices[0]["pci_address"], "0000:00:02.0")
        self.assertEqual(devices[0]["vendor_id"], "0x8086")
        self.assertEqual(devices[0]["device_id"], "0x9a49")

    def test_build_results_deduplicates_feature_entries(self):
        pci_map = {
            ("0x8086", "0x9a49"): [
                {"name": "GPU A", "media_feature": "MTL", "vendor_id": "0x8086"},
                {"name": "GPU B", "media_feature": "MTL", "vendor_id": "0x8086"},
            ]
        }
        feature_map = {
            "MTL": {
                "name": "MTL",
                "codecs": {
                    "decoders": [{"name": "h264", "max_resolution": "4k"}],
                    "encoders": [{"name": "h264", "max_resolution": "4k"}],
                },
            }
        }
        devices = [
            {
                "pci_address": "0000:00:02.0",
                "vendor_id": "0x8086",
                "device_id": "0x9a49",
            }
        ]

        results = mod.build_results(pci_map, feature_map, devices)

        self.assertEqual(len(results), 1)
        self.assertEqual(len(results[0]["matches"]), 2)
        self.assertEqual(len(results[0]["media_features"]), 1)
        self.assertEqual(results[0]["media_features"][0]["name"], "MTL")


if __name__ == "__main__":
    unittest.main()
