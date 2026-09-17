# Assumptions

This file details all the factors assumed during development.

- Each valid input line follows exactly one of the three supported formats.

- Format detection is based on the general structure and separators of each supported format. Field validity is checked separately. (regex)

- For Format B, the last word is treated as the `lastname`, and everything before it as the `firstname`.
For example. Incase of "Booker T. Washington", "Booker T." is considerated the firstname and "Washington" the lastname.

- Leading and trailing whitespace around comma-separated fields is ignored.