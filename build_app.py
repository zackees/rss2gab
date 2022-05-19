"""
    Builds the bigleague site.
"""

# pylint: disable=R1716

import os
import sys
import zipfile

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
APP_DIR = os.path.join(PROJECT_ROOT, "apps")

# Find all apps and ask the user which ones they want to build.
os.chdir(APP_DIR)

apps = [
    file.split(".")[0]
    for file in os.listdir(APP_DIR)
    if file.endswith(".py") and file != "build.py"
]
apps.sort()

print("\nAvailable apps:")
for i, app in enumerate(apps):
    print(f"  [{i}]: {app}")
user_input = input("\nWhich app would you like to build? ")
try:
    app_idx = int(user_input)
except ValueError:
    print(f"\nError, the input {user_input} was invalid. Exiting.\n")
    sys.exit(1)
assert app_idx >= 0 and app_idx < len(apps), f"Invalid app index: {app_idx}"
APP = apps[app_idx]


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
    "pip install nuitka zstandard",
    "&&",
    "pip install .",
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

print(
    f'\nDone building app "{APP_NAME}", binary located at:\n  {os.path.abspath(APP_NAME)}\n'
)
