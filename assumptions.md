# Assumptions

This file details all the factors assumed during development.

- Format detection is based on the general structure and separators of each supported format. Field validity is checked separately.

- For Format B, the last word is treated as the lastname, and everything before it as the firstname.
    For example. Incase of "Booker T. Washington", "Booker T." is treated as the firstname and "Washington" the lastname.

- Leading and trailing whitespace around comma-separated fields is ignored.

- Required text fields such as firstname, lastname, and color that are empty after trimming whitespace are treated as invalid records.
