import re
import json

FORMAT_A = r"[^,]+,\s*[^,]+,\s*\([^)]+\)-[^,\s]+-[^,\s]+,\s*[^,]+,\s*[^,]+"

FORMAT_B = r"[^,]+\s+[^,]+,\s*[^,]+,\s*[^,]+,\s*[^,\s]+\s+[^,\s]+\s+[^,\s]+"

FORMAT_C = r"[^,]+,\s*[^,]+,\s*[^,]+,\s*[^,\s]+\s+[^,\s]+\s+[^,\s]+,\s*[^,]+"

def get_digits(value):
    return "".join(char for char in value if char.isdigit())

def is_valid_zip(value):
    return len(value) == 5 and value.isdigit()

def is_valid_phone(value):
    return len(get_digits(value)) == 10

def is_valid_record(record):
    return (
        is_valid_zip(record["zipcode"])
        and is_valid_phone(record["phonenumber"])
    )

def split_name(full_name):
    name_parts = full_name.strip().split()

    if len(name_parts) < 2:
        return None

    firstname = " ".join(name_parts[:-1])
    lastname = name_parts[-1]

    return firstname, lastname

def detect_format(line):
    if re.fullmatch(FORMAT_A, line):
        return "A"

    if re.fullmatch(FORMAT_B, line):
        return "B"

    if re.fullmatch(FORMAT_C, line):
        return "C"

    return None

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

def normalize_phone(phone):
    digits = get_digits(phone)
    return f"{digits[:3]}-{digits[3:6]}-{digits[6:]}"

def normalize_zip(zipcode):
    return str(zipcode).strip()

def normalize_record(record):
    return {
        "firstname": record["firstname"],
        "lastname": record["lastname"],
        "phonenumber": normalize_phone(record["phonenumber"]),
        "color": record["color"],
        "zipcode": normalize_zip(record["zipcode"]),
    }

def main():
    errors = []
    entries = []
    with open("input.txt", "r", encoding="utf-8") as file:
        for index, line in enumerate(file):
            clean_line = line.strip()
            format_type = detect_format(clean_line)

            if format_type is None:
                #print(f"Line {index}: No format detected")
                errors.append(index)
                continue

            #print(f"Line {index}: Format {format_type}")

            parsed_record = parse_line(clean_line, format_type)
            if parsed_record is None or not is_valid_record(parsed_record):
                #print(f"Line {index}: Invalid line.")
                errors.append(index)
                continue

            #print(f"Line {index}: Valid line. Parsed data: {parsed_record}")
            normalized_record = normalize_record(parsed_record)
            entries.append(normalized_record)

    result = {
        "entries": entries,
        "errors": errors,
    }
    with open("result.json", "w", encoding="utf-8") as file:
        json.dump(result, file, indent=2, sort_keys=True)
    #print(f"Output: {result}")

if __name__ == "__main__":
    main()
