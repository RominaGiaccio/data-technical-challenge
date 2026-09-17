# data-technical-challenge
Python challenge for parsing, validating and normalizing personal information records.

## Challenge summary

The program reads personal information records from a text file. Each line may use one of three supported formats.

## Supported formats

```text
Lastname, Firstname, (XXX)-XXX-XXXX, Color, XXXXX
Firstname Lastname, Color, XXXXX, XXX XXX XXXX
Firstname, Lastname, XXXXX, XXX XXX XXXX, Color
```

## Requirements

- Read the input file line by line and support the three defined input formats.

- Parse each line into the following fields:
  - `firstname`
  - `lastname`
  - `phonenumber`
  - `color`
  - `zipcode`

- Validation and error handling:
  - phone number must contain exactly 10 digits
  - zip code must contain exactly 5 digits
  - lines that cannot be parsed reliably are invalid
  - invalid lines must not stop processing
  - store invalid 0-indexed line numbers in `errors`

- Normalize valid entries:
  - preserve names as-is
  - format phone numbers as `XXX-XXX-XXXX`
  - store zip codes as 5-character strings

- Sort valid entries in ascending alphabetical order by `(lastname, firstname)`.

- Write the result to `result.json` with exactly two top-level keys:
  - `entries`: list of normalized valid records
  - `errors`: list of invalid line numbers (0-indexed)

- Format the JSON with:
  - 2-space indentation
  - alphabetically sorted keys (at every object level)

# Setup

Requires Python 3.

Create a virtual environment:

```powershell
python -m venv .venv
```
Activate it:

```powershell
.venv\Scripts\Activate.ps1
```

Install test dependencies:

```powershell
pip install pytest
```

# Run

Pass the input file path as an argument:

```powershell
python main.py <input_file_path>
```

Example:

```powershell
python main.py input.txt
```

# Run tests

```powershell
pytest
```