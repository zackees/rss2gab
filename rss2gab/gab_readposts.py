"""
    Gab reader of account
"""
from typing import List

from garc.client import Garc  # type: ignore

DEFAULT_POST_LIMIT = 100


def gab_readposts(
    gab_id: str,
    gab_login_user: str,
    gab_login_pass: str,
    limit: int = DEFAULT_POST_LIMIT,
) -> List[str]:
    """Api to read the gab posts of the given user"""
    gab = Garc(user_account=gab_login_user, user_password=gab_login_pass)
    gab.login()
    posts = gab.userposts(gab_id, gabs=limit)
    out = []
    for post in posts:
        body = post["body"]
        if body:
            out.append(body)
    if limit != -1:
        out = out[:limit]
    return out


def unit_test() -> None:
    """Test runner"""
    out = gab_readposts(
        gab_id="testgabposter",
        gab_login_user="testgabposter",
        gab_login_pass="Yq4F2H9Lvp",
        limit=1,
    )
    print(out)


if __name__ == "__main__":
    unit_test()
