# Chapter 7, exercise 8: cross-reference the URLs in the input.
from _paths import use_chapter
from xref import write_xref, xref

use_chapter(6)
from find_urls import find_urls  # noqa: E402


def main():
    write_xref(xref(find_words=find_urls), plural_aware=True, wrap=15)


if __name__ == "__main__":
    main()
