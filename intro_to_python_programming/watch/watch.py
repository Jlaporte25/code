import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    # Regular expression to match the src attribute of an iframe with a YouTube embed URL
    pattern = r'<iframe[^>]*src="https?://(?:www\.)?youtube\.com/embed/([^"]+)"'

    match = re.search(pattern, s)
    if match:
        video_id = match.group(1)
        short_url = f"https://youtu.be/{video_id}"
        return short_url
    return None


if __name__ == "__main__":
    main()
