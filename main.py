import re

FORMAT_A = r"[^,]+,\s*[^,]+,\s*\(\d{3}\)-\d{3}-\d{4},\s*[^,]+,\s*\d{5}"

FORMAT_B = r"[^,]+\s+[^,]+,\s*[^,]+,\s*\d{5},\s*\d{3}\s+\d{3}\s+\d{4}"

FORMAT_C = r"[^,]+,\s*[^,]+,\s*\d{5},\s*\d{3}\s+\d{3}\s+\d{4},\s*[^,]+"

def detect_format(line):
    if re.fullmatch(FORMAT_A, line):
        return "A"

    if re.fullmatch(FORMAT_B, line):
        return "B"

    if re.fullmatch(FORMAT_C, line):
        return "C"

    return None


def main():
    with open("input.txt", "r", encoding="utf-8") as file:
        for index, line in enumerate(file):
            clean_line = line.strip()
            format_type = detect_format(clean_line)

            if format_type is None:
                print(f"Line {index}: No format detected")
                continue

            print(f"Line {index}: Format {format_type}")


if __name__ == "__main__":
    main()
