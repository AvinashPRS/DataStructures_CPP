# Chapter 7, exercise 7: write "line" or "lines" as appropriate.
from xref import write_xref, xref


def main():
    write_xref(xref(), plural_aware=True, wrap=15)


if __name__ == "__main__":
    main()
