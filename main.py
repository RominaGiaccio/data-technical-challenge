def detect_format(line):
    parts = [part.strip() for part in line.split(",")]

    if len(parts) == 4:
        return "format B"

    if len(parts) == 5:
        return "format A or C"

    return None

def main():
    with open("input.txt", "r") as file:
        for index, line in enumerate(file):
            clean_line = line.strip()
            format_type = detect_format(clean_line)
            result = f"line {index} _ {clean_line}: {format_type or 'No format detected'}"
            print(result)


if __name__ == "__main__":
    main()
