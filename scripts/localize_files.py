#!/usr/bin/env python3
"""Download and convert embed files for posts.  """

import argparse
import fileinput
import hashlib
import re
from pathlib import Path

import requests

__dirpath__ = Path(Path(__file__).parent.resolve())


def convert(text: str) -> str:
    ret = text
    match = re.findall(r'(https?://.+?\.(?:png|jpg|bmp))', ret)
    for i in set(match):
        print(i)
        ret = ret.replace(i,
                          '/' + download(i)
                          .relative_to(
                              __dirpath__
                              .parent)
                          .as_posix())

    return ret


def download(url) -> Path:
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        print(r.headers)
        dst = (__dirpath__.parent
               / 'images'
               / re.sub('[^\w_.)( -]', '', hashlib.sha1(bytes(r.headers['ETag'] or url, 'utf-8')).hexdigest())
               ).with_suffix('.' + r.headers['Content-Type'].split('/')[-1])
        if dst.exists():
            return dst
        with dst.open('wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)
    return dst


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('files', type=Path, nargs='+')

    args = parser.parse_args()
    for i in args.files:  # type: Path
        i.write_text(convert(i.read_text(encoding='utf-8')), encoding='utf-8')


if __name__ == '__main__':
    main()
