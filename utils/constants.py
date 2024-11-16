# Pillow format docs:
# https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html
ICO = "ico"
JPG = "jpg"
JPEG = "jpeg"
PNG = "png"
WEBP = "webp"
ALLOWED_EXTENSIONS = {ICO, JPG, JPEG, PNG, WEBP}
DEFAULT_QUALITY = 95
FORMAT_PARAMS = {
  ICO: [
    {
      "name": "sizes",
      "label": "Sizes",
      "description": "List of valid ICO sizes, in pixels.",
      "options": [
        [16, 16],
        [32, 32],
        [64, 64],
        [128, 128],
        [256, 256],
      ],
      "default": [128, 128]
    }
  ],
  JPEG: [
    {
      "name": "quality",
      "label": "Image quality",
      "description": "From 0 to 100. Higher is better, but larger size.",
      "min": 0,
      "max": 100,
      "default": DEFAULT_QUALITY
    },
    {
      "name": "optimize",
      "label": "Encoder optimization",
      "description": \
        "Optimize encoder settings. Improves quality at the cost of speed.",
      "is_bool": 1,
      "default": 0
    },
    {
      "name": "progressive",
      "label": "Progressive JPEG",
      "description": "Output a progressive JPEG file.",
      "is_bool": 1,
      "default": 0
    },
    {
      "name": "exif",
      "label": "Keep metadata",
      "description": \
        "Keep color profiles, EXIF and comments. This may increase file size.",
      "is_bool": 1,
      "default": 0
    }
  ],
  PNG: [
    {
      "name": "compress_level",
      "label": "Compression level",
      "description": \
        "From 0 to 9. Lower is faster convertion speed, but larger file size.",
      "min": 0,
      "max": 9,
      "default": 6
    },
    {
      "name": "exif",
      "label": "Keep metadata",
      "description": \
        "Keep color profiles, EXIF and comments. This may increase file size.",
      "is_bool": 1,
      "default": 0
    }
  ],
  WEBP: [
    {
      "name": "lossless",
      "label": "Lossless compression",
      "description": \
        "Compress without any quality loss. Can impact file size negatively.",
      "is_bool": 1,
      "default": 0
    },
    {
      "name": "quality",
      "depends_on": {
        "param_name": "lossless",
        "param_value": 0
      },
      "label": "Image quality",
      "description": "From 0 to 100. More is better, but larger size.",
      "min": 0,
      "max": 100,
      "default": DEFAULT_QUALITY
    },
    {
      "name": "method",
      "depends_on": {
        "param_name": "lossless",
        "param_value": 0
      },
      "label": "Compression speed",
      "description": \
        "Quality/speed tradeoff from 0 to 6. Higher is better, but slower.",
      "min": 0,
      "max": 6,
      "default": 4
    },
    {
      "name": "exif",
      "label": "Keep metadata",
      "description": \
        "Keep color profiles, EXIF and comments. This may increase file size.",
      "is_bool": 1,
      "default": 0
    }
  ]
}