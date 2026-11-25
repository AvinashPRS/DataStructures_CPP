# Chapter 7, exercise 4: break up long lists of line numbers.
from xref import write_xref, xref


def main():
    write_xref(xref(), wrap=15)


if __name__ == "__main__":
    main()
