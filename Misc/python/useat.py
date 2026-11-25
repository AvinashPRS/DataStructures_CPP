"""Accessing dictionary values (C++ std::map::at -> dict[key], raises if missing)."""


def main():
    age = {}
    age["Alice"] = 25
    age["Bob"] = 30
    print(age["Alice"])
    print(age["Bob"])


if __name__ == "__main__":
    main()
