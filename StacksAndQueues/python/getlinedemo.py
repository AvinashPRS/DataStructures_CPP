"""
Demo of splitting a string on a delimiter (Python equivalent of
std::getline on a stringstream with a custom delimiter).
"""

if __name__ == "__main__":
    # 1. Define the input string and the separator
    input_str = "Apple,Banana,Orange,Grape"
    delimiter = ","

    print("Starting to split the string...")
    print()

    # 2. str.split() yields the pieces one by one, like reading tokens from a stream
    for count, token in enumerate(input_str.split(delimiter), start=1):
        print(f"Loop Step {count}:")
        print(f"  Extracted piece (token): {token}")
        print("-------------------------")

    print("The stream is empty. Loop finished!")
