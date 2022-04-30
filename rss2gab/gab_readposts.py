"""
    Gab reader of account
"""
from typing import List

from garc.client import Garc  # type: ignore

DEFAULT_POST_LIMIT = 100


def gab_readposts(user: str, limit: int = DEFAULT_POST_LIMIT) -> List[str]:
    """Api to read the gab posts of the given user"""
    # g = Garc(user, "")
    gab = Garc()
    posts = gab.userposts(user, gabs=limit)
    out = []
    for post in posts:
        body = post["body"]
        if body:
            out.append(body)
    if limit != -1:
        out = out[:limit]
    return out


def main() -> None:
    """Test runner"""
    out = gab_readposts("perpetualmaniac", limit=1)
    print(out)


if __name__ == "__main__":
    main()
