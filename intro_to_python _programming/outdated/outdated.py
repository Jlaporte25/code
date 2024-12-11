import re
from datetime import datetime

def main():
    # List of month names
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    # Compile regex patterns for both date formats
    numeric_pattern = re.compile(r'^\d{1,2}/\d{1,2}/\d{4}$')
    textual_pattern = re.compile(r'^[A-Za-z]+ \d{1,2}, \d{4}$')

    while True:
        # Prompt the user for input
        date_str = input("Date: ").strip()

        try:
            # Try to match and parse the numeric format
            if numeric_pattern.match(date_str):
                date_obj = datetime.strptime(date_str, '%m/%d/%Y')
            # Try to match and parse the textual format
            elif textual_pattern.match(date_str):
                date_obj = datetime.strptime(date_str, '%B %d, %Y')
            else:
                raise ValueError()
            
            # Output the date in YYYY-MM-DD format
            print(f"{date_obj.strftime('%Y-%m-%d')}")
            break
        except ValueError:
            # If parsing fails, prompt the user again
            pass

if __name__ == "__main__":
    main()