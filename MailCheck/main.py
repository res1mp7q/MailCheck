import smtplib
import re
import py3dns

def get_mx_records(domain):
    try:
        mx_records = py3dns.resolver.query(domain, 'MX')
        return [str(mx.exchange)[:-1] for mx in mx_records]
    except (py3dns.resolver.NoAnswer, py3dns.resolver.NXDOMAIN, py3dns.resolver.NoNameservers) as e:
        print(f"Error resolving MX records for {domain}: {e}")
        return []

def get_a_records(domain):
    try:
        a_records = py3dns.resolver.query(domain, 'A')
        return [str(a) for a in a_records]
    except (py3dns.resolver.NoAnswer, py3dns.resolver.NXDOMAIN, py3dns.resolver.NoNameservers) as e:
        print(f"Error resolving A records for {domain}: {e}")
        return []

def print_domain_info(email):
    # Simple regex to check if the email address is in a valid format
    email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")
    if not email_regex.match(email):
        print("Invalid email address format.")
        return

    # Extract the domain from the email address
    _, domain = email.split('@')

    print(f"Domain: {domain}")

    # Get and print MX records for the domain
    mx_records = get_mx_records(domain)
    if mx_records:
        print("MX Records:")
        for mx in mx_records:
            print(f"- {mx}")
    else:
        print(f"No MX records found for {domain}")

    # Get and print A records for the domain
    a_records = get_a_records(domain)
    if a_records:
        print("A Records:")
        for a in a_records:
            print(f"- {a}")
    else:
        print(f"No A records found for {domain}")

if __name__ == "__main__":
    # Get the email address from the user
    user_email = input("Enter an email address: ")

    # Print domain information for the email address
    print_domain_info(user_email)
