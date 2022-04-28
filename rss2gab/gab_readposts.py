"""
    Gab reader of account
"""
import json
import subprocess
from typing import List

DEFAULT_POST_LIMIT = 100


def gab_readposts(user: str, limit: int = DEFAULT_POST_LIMIT) -> List[str]:
    """Api to read the gab posts of the given user"""
    cmd = ["garc", "userposts", user, f"--number_gabs={limit}"]
    stdout = subprocess.check_output(cmd, universal_newlines=True)
    lines = stdout.split("\n")
    lines = [line for line in lines if line.startswith("{")]
    titles = []
    for line in lines:
        try:
            data = json.loads(line)
            body = data["body"]
            if body:
                titles.append(body)
        except Exception as err:  # pylint: disable=broad-except
            print(
                f"{__file__}: Warning, bad characters in json: {err}, while parsing {line}"
            )
    return titles
