import os
from functools import lru_cache

from zk_observer.settings import TEMPLATE_DIR


def get_full_template_path(template_name: str) -> str:
    return os.path.join(TEMPLATE_DIR, template_name + '.html')


@lru_cache(maxsize=None)
def get_index_page_content() -> str:
    with open(get_full_template_path('index')) as f:
        return f.read()
