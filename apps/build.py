"""
    Builds the bigleague site.
"""

import os
import sys
import zipfile

APP = "generic"

HERE = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(HERE)


os.chdir(PROJECT_ROOT)

if not os.path.exists("activate.sh"):
    rtn = os.system("./install_dev.sh")
    if rtn != 0:
        print("Failed to install")
        sys.exit(rtn)

APP_BUILD_DIR = os.path.join("apps", "build", APP)
APP_SRC = os.path.join("apps", f"{APP}.py")
APP_NAME = f"{APP}"
if sys.platform == "win32":
    APP_NAME += ".exe"

os.makedirs(APP_BUILD_DIR, exist_ok=True)

CMD = [
    ". activate.sh",
    "&&",
    "pip install nuitka zstandard",
    "&&",
    "pip install .",
    "&&",
    "rss2gab_selenium_install",
    "&&",
    "python -m nuitka",
    "--follow-imports",
    "--standalone",
    "--include-package-data=selenium,rss2gab",
    f"--output-dir={APP_BUILD_DIR}",
    APP_SRC,
    "--onefile",
    "-o",
    f"{APP_BUILD_DIR}/{APP_NAME}",
]
CMD_STR = " ".join(CMD)

print(f"Executing:\n  {CMD_STR}")
rtn = os.system(CMD_STR)

if rtn != 0:
    print("Failed to build")
    sys.exit(rtn)

os.chdir(APP_BUILD_DIR)

# make a zip file of the APP_NAME at the current directory
with zipfile.ZipFile(f"{APP_NAME}.zip", "w", zipfile.ZIP_DEFLATED) as zipf:
    zipf.write(APP_NAME)
