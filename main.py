def main():
    with open("input.txt", "r") as file:
        for index, line in enumerate(file):
            print(index, line.strip())


if __name__ == "__main__":
    main()