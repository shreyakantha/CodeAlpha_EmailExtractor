import re
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def extract_emails(input_file, output_file):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'

    input_path = os.path.join(BASE_DIR, input_file)
    output_path = os.path.join(BASE_DIR, output_file)

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: {input_file} not found.")
        return

    emails = re.findall(email_pattern, content)
    unique_emails = sorted(set(emails))

    with open(output_path, 'w', encoding='utf-8') as file:
        for email in unique_emails:
            file.write(email + '\n')

    print(f"Extracted {len(unique_emails)} unique email(s) to {output_file}")

extract_emails('input.txt', 'emails.log')
