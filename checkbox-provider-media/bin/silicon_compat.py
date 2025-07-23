#!/usr/bin/env python3

import sys

from parse_vainfo import get_codec_support_dict
from intel_gen import get_media_driver_category, get_media_driver_category
from huc_check import is_huc_running

def get_platform_support_dict(is_huc_active=True):
    # Defined in the table at
    # https://github.com/intel/media-driver?tab=readme-ov-file#decodingencoding-features
    return {
        "PTL" : {
            "AVC" : {
                "encode" : True,
                "decode" : True
                },
            "MPEG-2" : {
                "encode" : False,
                "decode" : True
                },
            "VC-1" : {
                "encode" : False,
                "decode" : False
                },
            "JPEG" : {
                "encode" : True,
                "decode" : True
                },
            "VP8" : {
                "encode" : False,
                "decode" : True
                },
            "HEVC 8-bit" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "HEVC 8bit 422" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "HEVC 8bit 444" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "HEVC 10bit" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "HEVC 10bit 422" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "HEVC 10bit 444" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "HEVC 12bit" : {
                "encode" : False,
                "decode" : True
                },
            "HEVC 12bit 422" : {
                "encode" : False,
                "decode" : True
                },
            "HEVC 12bit 444" : {
                "encode" : False,
                "decode" : True
                },
            "VP9 8bit" : {
                "encode" : False,
                "decode" : True
                },
            "VP9 8bit 444" : {
                "encode" : False,
                "decode" : True
                },
            "VP9 10bit" : {
                "encode" : False,
                "decode" : True
                },
            "VP9 10bit 444" : {
                "encode" : False,
                "decode" : True
                },
            "VP9 12bit" : {
                "encode" : False,
                "decode" : True
                },
            "VP9 12bit 444" : {
                "encode" : False,
                "decode" : True
                },
            "AV1 8bit" : {
                "encode" : True,
                "decode" : True
                },
            "AV1 10bit" : {
                "encode" : True,
                "decode" : True
                },
            "VVC 8bit" : {
                "encode" : False,
                "decode" : False
                },
            "VVC 10bit" : {
                "encode" : False,
                "decode" : False
                }
            },
        "BMG" : {
            "AVC" : {
                "encode" : True,
                "decode" : True
                },
            "MPEG-2" : {
                "encode" : False,
                "decode" : False
                },
            "VC-1" : {
                "encode" : False,
                "decode" : False
                },
            "JPEG" : {
                "encode" : True,
                "decode" : True
                },
            "VP8" : {
                "encode" : False,
                "decode" : True
                },
            "HEVC 8-bit" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "HEVC 8bit 422" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "HEVC 8bit 444" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "HEVC 10bit" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "HEVC 10bit 422" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "HEVC 10bit 444" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "HEVC 12bit" : {
                "encode" : False,
                "decode" : True
                },
            "HEVC 12bit 422" : {
                "encode" : False,
                "decode" : True
                },
            "HEVC 12bit 444" : {
                "encode" : False,
                "decode" : True
                },
            "VP9 8bit" : {
                "encode" : False,
                "decode" : True
                },
            "VP9 8bit 444" : {
                "encode" : False,
                "decode" : True
                },
            "VP9 10bit" : {
                "encode" : False,
                "decode" : True
                },
            "VP9 10bit 444" : {
                "encode" : False,
                "decode" : True
                },
            "VP9 12bit" : {
                "encode" : False,
                "decode" : True
                },
            "VP9 12bit 444" : {
                "encode" : False,
                "decode" : True
                },
            "AV1 8bit" : {
                "encode" : True,
                "decode" : True
                },
            "AV1 10bit" : {
                "encode" : True,
                "decode" : True
                },
            "VVC 8bit" : {
                "encode" : False,
                "decode" : False
                },
            "VVC 10bit" : {
                "encode" : False,
                "decode" : False
                }
            },
        "LNL" : {
            "AVC" : {
                "encode" : True,
                "decode" : True
                },
            "MPEG-2" : {
                "encode" : False,
                "decode" : True
                },
            "VC-1" : {
                "encode" : False,
                "decode" : False
                },
            "JPEG" : {
                "encode" : True,
                "decode" : True
                },
            "VP8" : {
                "encode" : False,
                "decode" : True
                },
            "HEVC 8-bit" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "HEVC 8bit 422" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "HEVC 8bit 444" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "HEVC 10bit" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "HEVC 10bit 422" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "HEVC 10bit 444" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "HEVC 12bit" : {
                "encode" : False,
                "decode" : True
                },
            "HEVC 12bit 422" : {
                "encode" : False,
                "decode" : True
                },
            "HEVC 12bit 444" : {
                "encode" : False,
                "decode" : True
                },
            "VP9 8bit" : {
                "encode" : False,
                "decode" : True
                },
            "VP9 8bit 444" : {
                "encode" : False,
                "decode" : True
                },
            "VP9 10bit" : {
                "encode" : False,
                "decode" : True
                },
            "VP9 10bit 444" : {
                "encode" : False,
                "decode" : True
                },
            "VP9 12bit" : {
                "encode" : False,
                "decode" : True
                },
            "VP9 12bit 444" : {
                "encode" : False,
                "decode" : True
                },
            "AV1 8bit" : {
                "encode" : True,
                "decode" : True
                },
            "AV1 10bit" : {
                "encode" : True,
                "decode" : True
                },
            "VVC 8bit" : {
                "encode" : False,
                "decode" : True
                },
            "VVC 10bit" : {
                "encode" : False,
                "decode" : True
                }
            },
        "MTLx" : {
            "AVC" : {
                "encode" : True,
                "decode" : True
                },
            "MPEG-2" : {
                "encode" : False,
                "decode" : True
                },
            "VC-1" : {
                "encode" : False,
                "decode" : False
                },
            "JPEG" : {
                "encode" : True,
                "decode" : True
                },
            "VP8" : {
                "encode" : False,
                "decode" : True
                },
            "HEVC 8-bit" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "HEVC 8bit 422" : {
                "encode" : False,
                "decode" : True
                },
            "HEVC 8bit 444" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "HEVC 10bit" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "HEVC 10bit 422" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "HEVC 10bit 444" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "HEVC 12bit" : {
                "encode" : False,
                "decode" : True
                },
            "HEVC 12bit 422" : {
                "encode" : False,
                "decode" : True
                },
            "HEVC 12bit 444" : {
                "encode" : False,
                "decode" : True
                },
            "VP9 8bit" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "VP9 8bit 444" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "VP9 10bit" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "VP9 10bit 444" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "VP9 12bit" : {
                "encode" : False and is_huc_active,
                "decode" : True
                },
            "VP9 12bit 444" : {
                "encode" : False and is_huc_active,
                "decode" : True
                },
            "AV1 8bit" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "AV1 10bit" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "VVC 8bit" : {
                "encode" : False,
                "decode" : False
                },
            "VVC 10bit" : {
                "encode" : False,
                "decode" : False
                }
            },
        "DG2/ATSM" : {
            "AVC" : {
                "encode" : True,
                "decode" : True
                },
            "MPEG-2" : {
                "encode" : False,
                "decode" : True
                },
            "VC-1" : {
                "encode" : False,
                "decode" : False
                },
            "JPEG" : {
                "encode" : True,
                "decode" : True
                },
            "VP8" : {
                "encode" : False,
                "decode" : False
                },
            "HEVC 8-bit" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "HEVC 8bit 422" : {
                "encode" : False,
                "decode" : True
                },
            "HEVC 8bit 444" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "HEVC 10bit" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "HEVC 10bit 422" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "HEVC 10bit 444" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "HEVC 12bit" : {
                "encode" : False,
                "decode" : True
                },
            "HEVC 12bit 422" : {
                "encode" : False,
                "decode" : True
                },
            "HEVC 12bit 444" : {
                "encode" : False,
                "decode" : True
                },
            "VP9 8bit" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "VP9 8bit 444" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "VP9 10bit" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "VP9 10bit 444" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "VP9 12bit" : {
                "encode" : False and is_huc_active,
                "decode" : True
                },
            "VP9 12bit 444" : {
                "encode" : False and is_huc_active,
                "decode" : True
                },
            "AV1 8bit" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "AV1 10bit" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "VVC 8bit" : {
                "encode" : False,
                "decode" : False
                },
            "VVC 10bit" : {
                "encode" : False,
                "decode" : False
                }
            },
        "DG1/SG1" : {
            "AVC" : {
                "encode" : True,
                "decode" : True
                },
            "MPEG-2" : {
                "encode" : True,
                "decode" : True
                },
            "VC-1" : {
                "encode" : False,
                "decode" : True
                },
            "JPEG" : {
                "encode" : True,
                "decode" : True
                },
            "VP8" : {
                "encode" : False,
                "decode" : False
                },
            "HEVC 8-bit" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "HEVC 8bit 422" : {
                "encode" : False,
                "decode" : True
                },
            "HEVC 8bit 444" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "HEVC 10bit" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "HEVC 10bit 422" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "HEVC 10bit 444" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "HEVC 12bit" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "HEVC 12bit 422" : {
                "encode" : False,
                "decode" : True
                },
            "HEVC 12bit 444" : {
                "encode" : False,
                "decode" : True
                },
            "VP9 8bit" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "VP9 8bit 444" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "VP9 10bit" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "VP9 10bit 444" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "VP9 12bit" : {
                "encode" : False,
                "decode" : True
                },
            "VP9 12bit 444" : {
                "encode" : False,
                "decode" : True
                },
            "AV1 8bit" : {
                "encode" : False,
                "decode" : True
                },
            "AV1 10bit" : {
                "encode" : False,
                "decode" : True
                },
            "VVC 8bit" : {
                "encode" : False,
                "decode" : False
                },
            "VVC 10bit" : {
                "encode" : False,
                "decode" : False
                }
            },    
        "TGLx" : {
            "AVC" : {
                "encode" : True,
                "decode" : True
                },
            "MPEG-2" : {
                "encode" : True,
                "decode" : True
                },
            "VC-1" : {
                "encode" : False,
                "decode" : True
                },
            "JPEG" : {
                "encode" : True,
                "decode" : True
                },
            "VP8" : {
                "encode" : False,
                "decode" : True
                },
            "HEVC 8-bit" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "HEVC 8bit 422" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "HEVC 8bit 444" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "HEVC 10bit" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "HEVC 10bit 422" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "HEVC 10bit 444" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "HEVC 12bit" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "HEVC 12bit 422" : {
                "encode" : False,
                "decode" : True
                },
            "HEVC 12bit 444" : {
                "encode" : False,
                "decode" : True
                },
            "VP9 8bit" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "VP9 8bit 444" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "VP9 10bit" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "VP9 10bit 444" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "VP9 12bit" : {
                "encode" : False,
                "decode" : True
                },
            "VP9 12bit 444" : {
                "encode" : False,
                "decode" : True
                },
            "AV1 8bit" : {
                "encode" : False,
                "decode" : True
                },
            "AV1 10bit" : {
                "encode" : False,
                "decode" : True
                },
            "VVC 8bit" : {
                "encode" : False,
                "decode" : False
                },
            "VVC 10bit" : {
                "encode" : False,
                "decode" : False
                }
            },
        "EHL/JSL" : {
            "AVC" : {
                "encode" : True,
                "decode" : True
                },
            "MPEG-2" : {
                "encode" : False,
                "decode" : True
                },
            "VC-1" : {
                "encode" : False,
                "decode" : True
                },
            "JPEG" : {
                "encode" : True,
                "decode" : True
                },
            "VP8" : {
                "encode" : False,
                "decode" : True
                },
            "HEVC 8-bit" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "HEVC 8bit 422" : {
                "encode" : False,
                "decode" : True
                },
            "HEVC 8bit 444" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "HEVC 10bit" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "HEVC 10bit 422" : {
                "encode" : False,
                "decode" : True
                },
            "HEVC 10bit 444" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "HEVC 12bit" : {
                "encode" : False,
                "decode" : False
                },
            "HEVC 12bit 422" : {
                "encode" : False,
                "decode" : False
                },
            "HEVC 12bit 444" : {
                "encode" : False,
                "decode" : False
                },
            "VP9 8bit" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "VP9 8bit 444" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "VP9 10bit" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "VP9 10bit 444" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "VP9 12bit" : {
                "encode" : False,
                "decode" : False
                },
            "VP9 12bit 444" : {
                "encode" : False,
                "decode" : False
                },
            "AV1 8bit" : {
                "encode" : False,
                "decode" : False
                },
            "AV1 10bit" : {
                "encode" : False,
                "decode" : False
                },
            "VVC 8bit" : {
                "encode" : False,
                "decode" : False
                },
            "VVC 10bit" : {
                "encode" : False,
                "decode" : False
                }
            },
        "ICL" : {
            "AVC" : {
                "encode" : True,
                "decode" : True
                },
            "MPEG-2" : {
                "encode" : True,
                "decode" : True
                },
            "VC-1" : {
                "encode" : False,
                "decode" : True
                },
            "JPEG" : {
                "encode" : True,
                "decode" : True
                },
            "VP8" : {
                "encode" : True,
                "decode" : True
                },
            "HEVC 8-bit" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "HEVC 8bit 422" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "HEVC 8bit 444" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "HEVC 10bit" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "HEVC 10bit 422" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "HEVC 10bit 444" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "HEVC 12bit" : {
                "encode" : False,
                "decode" : False
                },
            "HEVC 12bit 422" : {
                "encode" : False,
                "decode" : False
                },
            "HEVC 12bit 444" : {
                "encode" : False,
                "decode" : False
                },
            "VP9 8bit" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "VP9 8bit 444" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "VP9 10bit" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "VP9 10bit 444" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "VP9 12bit" : {
                "encode" : False,
                "decode" : False
                },
            "VP9 12bit 444" : {
                "encode" : False,
                "decode" : False
                },
            "AV1 8bit" : {
                "encode" : False,
                "decode" : False
                },
            "AV1 10bit" : {
                "encode" : False,
                "decode" : False
                },
            "VVC 8bit" : {
                "encode" : False,
                "decode" : False
                },
            "VVC 10bit" : {
                "encode" : False,
                "decode" : False
                }
            },
        "KBLx" : {
            "AVC" : {
                "encode" : True,
                "decode" : True
                },
            "MPEG-2" : {
                "encode" : True,
                "decode" : True
                },
            "VC-1" : {
                "encode" : False,
                "decode" : True
                },
            "JPEG" : {
                "encode" : True,
                "decode" : True
                },
            "VP8" : {
                "encode" : True,
                "decode" : True
                },
            "HEVC 8-bit" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "HEVC 8bit 422" : {
                "encode" : False,
                "decode" : False
                },
            "HEVC 8bit 444" : {
                "encode" : False,
                "decode" : False
                },
            "HEVC 10bit" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "HEVC 10bit 422" : {
                "encode" : False,
                "decode" : False
                },
            "HEVC 10bit 444" : {
                "encode" : False,
                "decode" : False
                },
            "HEVC 12bit" : {
                "encode" : False,
                "decode" : False
                },
            "HEVC 12bit 422" : {
                "encode" : False,
                "decode" : False
                },
            "HEVC 12bit 444" : {
                "encode" : False,
                "decode" : False
                },
            "VP9 8bit" : {
                "encode" : False,
                "decode" : True
                },
            "VP9 8bit 444" : {
                "encode" : False,
                "decode" : False
                },
            "VP9 10bit" : {
                "encode" : False,
                "decode" : True
                },
            "VP9 10bit 444" : {
                "encode" : False,
                "decode" : False
                },
            "VP9 12bit" : {
                "encode" : False,
                "decode" : False
                },
            "VP9 12bit 444" : {
                "encode" : False,
                "decode" : False
                },
            "AV1 8bit" : {
                "encode" : False,
                "decode" : False
                },
            "AV1 10bit" : {
                "encode" : False,
                "decode" : False
                },
            "VVC 8bit" : {
                "encode" : False,
                "decode" : False
                },
            "VVC 10bit" : {
                "encode" : False,
                "decode" : False
                }
            },
        "BXTx" : {
            "AVC" : {
                "encode" : True,
                "decode" : True
                },
            "MPEG-2" : {
                "encode" : False,
                "decode" : True
                },
            "VC-1" : {
                "encode" : False,
                "decode" : True
                },
            "JPEG" : {
                "encode" : True,
                "decode" : True
                },
            "VP8" : {
                "encode" : False,
                "decode" : True
                },
            "HEVC 8-bit" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "HEVC 8bit 422" : {
                "encode" : False,
                "decode" : False
                },
            "HEVC 8bit 444" : {
                "encode" : False,
                "decode" : False
                },
            "HEVC 10bit" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "HEVC 10bit 422" : {
                "encode" : False,
                "decode" : False
                },
            "HEVC 10bit 444" : {
                "encode" : False,
                "decode" : False
                },
            "HEVC 12bit" : {
                "encode" : False,
                "decode" : False
                },
            "HEVC 12bit 422" : {
                "encode" : False,
                "decode" : False
                },
            "HEVC 12bit 444" : {
                "encode" : False,
                "decode" : False
                },
            "VP9 8bit" : {
                "encode" : False,
                "decode" : True
                },
            "VP9 8bit 444" : {
                "encode" : False,
                "decode" : False
                },
            "VP9 10bit" : {
                "encode" : False,
                "decode" : False
                },
            "VP9 10bit 444" : {
                "encode" : False,
                "decode" : False
                },
            "VP9 12bit" : {
                "encode" : False,
                "decode" : False
                },
            "VP9 12bit 444" : {
                "encode" : False,
                "decode" : False
                },
            "AV1 8bit" : {
                "encode" : False,
                "decode" : False
                },
            "AV1 10bit" : {
                "encode" : False,
                "decode" : False
                },
            "VVC 8bit" : {
                "encode" : False,
                "decode" : False
                },
            "VVC 10bit" : {
                "encode" : False,
                "decode" : False
                }
            },
        "SKL" : {
            "AVC" : {
                "encode" : True,
                "decode" : True
                },
            "MPEG-2" : {
                "encode" : True,
                "decode" : True
                },
            "VC-1" : {
                "encode" : False,
                "decode" : True
                },
            "JPEG" : {
                "encode" : True,
                "decode" : True
                },
            "VP8" : {
                "encode" : False,
                "decode" : True
                },
            "HEVC 8-bit" : {
                "encode" : True and is_huc_active,
                "decode" : True
                },
            "HEVC 8bit 422" : {
                "encode" : False,
                "decode" : False
                },
            "HEVC 8bit 444" : {
                "encode" : False,
                "decode" : False
                },
            "HEVC 10bit" : {
                "encode" : False,
                "decode" : False
                },
            "HEVC 10bit 422" : {
                "encode" : False,
                "decode" : False
                },
            "HEVC 10bit 444" : {
                "encode" : False,
                "decode" : False
                },
            "HEVC 12bit" : {
                "encode" : False,
                "decode" : False
                },
            "HEVC 12bit 422" : {
                "encode" : False,
                "decode" : False
                },
            "HEVC 12bit 444" : {
                "encode" : False,
                "decode" : False
                },
            "VP9 8bit" : {
                "encode" : False,
                "decode" : False
                },
            "VP9 8bit 444" : {
                "encode" : False,
                "decode" : False
                },
            "VP9 10bit" : {
                "encode" : False,
                "decode" : False
                },
            "VP9 10bit 444" : {
                "encode" : False,
                "decode" : False
                },
            "VP9 12bit" : {
                "encode" : False,
                "decode" : False
                },
            "VP9 12bit 444" : {
                "encode" : False,
                "decode" : False
                },
            "AV1 8bit" : {
                "encode" : False,
                "decode" : False
                },
            "AV1 10bit" : {
                "encode" : False,
                "decode" : False
                },
            "VVC 8bit" : {
                "encode" : False,
                "decode" : False
                },
            "VVC 10bit" : {
                "encode" : False,
                "decode" : False
                }
            },
        "BDW" : {
            "AVC" : {
                "encode" : True,
                "decode" : True
                },
            "MPEG-2" : {
                "encode" : True,
                "decode" : True
                },
            "VC-1" : {
                "encode" : False,
                "decode" : True
                },
            "JPEG" : {
                "encode" : False,
                "decode" : True
                },
            "VP8" : {
                "encode" : False,
                "decode" : True
                },
            "HEVC 8-bit" : {
                "encode" : False,
                "decode" : False
                },
            "HEVC 8bit 422" : {
                "encode" : False,
                "decode" : False
                },
            "HEVC 8bit 444" : {
                "encode" : False,
                "decode" : False
                },
            "HEVC 10bit" : {
                "encode" : False,
                "decode" : False
                },
            "HEVC 10bit 422" : {
                "encode" : False,
                "decode" : False
                },
            "HEVC 10bit 444" : {
                "encode" : False,
                "decode" : False
                },
            "HEVC 12bit" : {
                "encode" : False,
                "decode" : False
                },
            "HEVC 12bit 422" : {
                "encode" : False,
                "decode" : False
                },
            "HEVC 12bit 444" : {
                "encode" : False,
                "decode" : False
                },
            "VP9 8bit" : {
                "encode" : False,
                "decode" : False
                },
            "VP9 8bit 444" : {
                "encode" : False,
                "decode" : False
                },
            "VP9 10bit" : {
                "encode" : False,
                "encode" : False,
                "decode" : False
                },
            "VP9 12bit 444" : {
                "encode" : False,
                "decode" : False
                },
            "AV1 8bit" : {
                "encode" : False,
                "decode" : False
                },
            "AV1 10bit" : {
                "encode" : False,
                "decode" : False
                },
            "VVC 8bit" : {
                "encode" : False,
                "decode" : False
                },
            "VVC 10bit" : {
                "encode" : False,
                "decode" : False
                }
            }
        }

def diff_vainfo_vs_support_table():
    huc_running = is_huc_running()
    platform_support = get_platform_support_dict(huc_running)
    media_driver_gpu_category = get_media_driver_category()
    platform_support_for_gpu = platform_support[media_driver_gpu_category]

    codec_support_dict = get_codec_support_dict()

    failed_checks = {}
    for codec in platform_support_for_gpu:
        if codec in codec_support_dict:
            for operation in ["encode", "decode"]:
                if codec_support_dict[codec][operation] != platform_support_for_gpu[codec][operation]:
                    failed_checks[codec] = operation

    if(len(failed_checks.keys()) != 0):
        print("Failed: Support in the Intel media driver table does not match vainfo", file=sys.stderr)
        for codec in failed_checks:
            print("A mismatch has occured for %s for the %s operation" % (codec, failed_checks[codec]))
        print("Please check your support for your platform (%s) here:" % get_media_driver_category(), file=sys.stderr)
        print("\thttps://github.com/intel/media-driver?tab=readme-ov-file#decodingencoding-features", file=sys.stderr)
        exit(1)

if __name__ == "__main__":
    diff_vainfo_vs_support_table()
