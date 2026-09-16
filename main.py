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

def split_name(full_name):
    name_parts = full_name.strip().split()

    if len(name_parts) < 2:
        return None

    firstname = " ".join(name_parts[:-1])
    lastname = name_parts[-1]

    return firstname, lastname

def parse_format_a(parts):
    return {
        "firstname": parts[1],
        "lastname": parts[0],
        "phonenumber": parts[2],
        "color": parts[3],
        "zipcode": parts[4],
    }

def parse_format_b(parts):
    name = split_name(parts[0])

    if name is None:
        return None

    firstname, lastname = name
    return {
        "firstname": firstname,
        "lastname": lastname,
        "phonenumber": parts[3],
        "color": parts[1],
        "zipcode": parts[2],
    }

def parse_format_c(parts):
    return {
        "firstname": parts[0],
        "lastname": parts[1],
        "phonenumber": parts[3],
        "color": parts[4],
        "zipcode": parts[2],
    }

def parse_line(clean_line, format_type):
    parts = [part.strip() for part in clean_line.split(",")]

    if format_type == "A":
        return parse_format_a(parts)

    if format_type == "B":
        return parse_format_b(parts)

    if format_type == "C":
        return parse_format_c(parts)

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

            result = parse_line(clean_line, format_type)
            if result:
                print(f"Line {index}: Parsed data - {result}")


if __name__ == "__main__":
    main()
