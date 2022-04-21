"""
system commands related to github
"""

import os
from dotenv import load_dotenv

load_dotenv()


def get_github_token():
    """
    from environment
    """
    return os.environ.get("GITHUB_TOKEN")
