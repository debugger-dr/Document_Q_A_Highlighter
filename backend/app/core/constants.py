import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UPLOAD_DIRECTORY = os.path.join(BASE_DIR, "data/uploads")
PROCESSED_DIRECTORY = os.path.join(BASE_DIR, "data/processed_pdfs")
HIGHLIGHTED_OUTPUT_DIRECTORY = os.path.join(BASE_DIR, "data/highlighted")
OCRMYPDF_TEXT_DIRECTORY = os.path.join(BASE_DIR, "data/ocrmypdf_text")
LAYOUTPARSER_TEXT_DIRECTORY = os.path.join(BASE_DIR, "data/layoutparser_text")
MODELS_DIRECTORY = os.path.join(BASE_DIR, "models")
CONFIG_PATH = os.path.join(os.path.dirname(__file__), "faster_rcnn_R_50_FPN_3x.yaml")
WEIGHTS_PATH = "/Users/dev/.torch/iopath_cache/s/dgy9c10wykk4lq4/model_final.pth"
