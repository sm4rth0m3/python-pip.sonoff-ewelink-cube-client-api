#!/bin/sh

# Check for non-breaking spaces in a file
check_non_breaking_spaces() {
    file=$1

    if grep -Pq "\x{00A0}" "$file"; then
        echo "Non-breaking spaces found in file: $file"
        echo "Please remove non-breaking spaces before committing."

        # Print the location of the character in the file
        grep -Pn "\x{00A0}" "$file"

        exit 1
    fi
}

check_non_breaking_spaces "$1"

exit 0
