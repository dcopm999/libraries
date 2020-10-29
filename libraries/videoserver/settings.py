import os
import logging


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

TEMPLATE_ROOT = os.path.join(BASE_DIR, "templates")

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

