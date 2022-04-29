"""
    Builds the bigleague site.
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(HERE)

os.chdir(PROJECT_ROOT)

if not os.path.exists("activate.sh"):
    rtn = os.system("./install_dev.sh")
    if rtn != 0:
        print("Failed to install")
        sys.exit(rtn)

# APP = "bigleague"
APP = "bigleague"

APP_BUILD_DIR = os.path.join(PROJECT_ROOT, "apps", "build", APP)
APP_SRC = os.path.join(PROJECT_ROOT, "apps", f"{APP}.py")
APP_NAME = f"{APP}"
if sys.platform == "win32":
    APP_NAME += ".exe"

os.makedirs(APP_BUILD_DIR, exist_ok=True)

CMD = [
    ". activate.sh",
    "&&",
    "pip install nuitka zstandard",
    "&&",
    f"cd {APP_BUILD_DIR}",
    "&&",
    "python -m nuitka",
    "--follow-imports",
    "--standalone",
    "--include-package-data=selenium",
    APP_SRC,
    "--onefile",
    "-o",
    APP_NAME,
]

CMD_STR = " ".join(CMD)

print(f"Executing:\n  {CMD_STR}")
rtn = os.system(CMD_STR)

if rtn != 0:
    print("Failed to build")
    sys.exit(rtn)
