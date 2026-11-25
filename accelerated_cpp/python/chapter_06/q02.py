# Chapter 6, exercise 2: test find_urls.
from find_urls import find_urls


def main():
    test = ("Hello, welcome to my GitHub! The link to my"
            "repository is https://github.com/altugbakan/accelerated-cpp-solutions"
            " and the link to the book's website is http://www.acceleratedcpp.com/")
    print("Found URLs are: ")
    for url in find_urls(test):
        print(url)


if __name__ == "__main__":
    main()
