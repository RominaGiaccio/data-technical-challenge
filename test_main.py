from main import (
    detect_format,
    is_valid_phone, 
    is_valid_record,
    is_valid_zip, 
    normalize_phone,
    normalize_record, 
    parse_line
)

# Format detection

def test_detect_format_a():
    line = "Washington, Booker T., (703)-742-0996, Blue, 10013"
    assert detect_format(line) == "A"

def test_detect_format_b():
    line = "James Murphy, Red, 11237, 703 955 0373"
    assert detect_format(line) == "B"

def test_detect_format_c():
    line = "Kerri, Chandler, 10013, 646 111 0101, Green"
    assert detect_format(line) == "C"

def test_invalid_format():
    line = "error500"

    assert detect_format(line) is None

# Validation

def test_invalid_zip():
    assert is_valid_zip("123123121") is False

def test_invalid_phone():
    assert is_valid_phone("703 955 037") is False

# Normalization

def test_normalize_phone():
    assert normalize_phone("703 955 0373") == "703-955-0373"

# Full line processing

def test_process_valid_format_a():
    line = "Washington, Booker T., (703)-742-0996, Blue, 10013"

    format_type = detect_format(line)
    record = parse_line(line, format_type)

    assert format_type == "A"
    assert is_valid_record(record) is True

    normalized = normalize_record(record)

    assert normalized == {
        "firstname": "Booker T.",
        "lastname": "Washington",
        "phonenumber": "703-742-0996",
        "color": "Blue",
        "zipcode": "10013",
    }

def test_process_valid_format_b():
    line = "Booker T. Washington, yellow, 83880, 018 154 6474"

    format_type = detect_format(line)
    record = parse_line(line, format_type)

    assert format_type == "B"
    assert is_valid_record(record) is True

    normalized = normalize_record(record)

    assert normalized == {
        "firstname": "Booker T.",
        "lastname": "Washington",
        "phonenumber": "018-154-6474",
        "color": "yellow",
        "zipcode": "83880",
    }

def test_process_valid_format_c():
    line = "Kerri, Chandler, 10013, 646 111 0101, Green"

    format_type = detect_format(line)
    record = parse_line(line, format_type)

    assert format_type == "C"
    assert is_valid_record(record) is True

    normalized = normalize_record(record)

    assert normalized == {
        "firstname": "Kerri",
        "lastname": "Chandler",
        "phonenumber": "646-111-0101",
        "color": "Green",
        "zipcode": "10013",
    }

def test_valid_format_with_invalid_zip():
    line = "Chandler, Kerri, (623)-668-9293, pink, 123123121"

    format_type = detect_format(line)
    record = parse_line(line, format_type)

    assert format_type == "A"
    assert is_valid_record(record) is False

def test_valid_format_with_invalid_phone():
    line = "Chandler, Kerri, (623)-668-929, pink, 12312"

    format_type = detect_format(line)
    record = parse_line(line, format_type)

    assert format_type == "A"
    assert is_valid_record(record) is False

def test_process_valid_format_with_large_name():
    line = "Ana Maria Paula Holmes, yellow, 83880, 018 154 6474"

    format_type = detect_format(line)
    record = parse_line(line, format_type)

    assert format_type == "B"
    assert is_valid_record(record) is True

    normalized = normalize_record(record)

    assert normalized == {
        "firstname": "Ana Maria Paula",
        "lastname": "Holmes",
        "phonenumber": "018-154-6474",
        "color": "yellow",
        "zipcode": "83880",
    }