import re


def extract_accessions(text):
    matches = re.findall(r"GSE\d+|SRP\d+|SRX\d+", text)
    unique_matches = list(dict.fromkeys(matches))
    return unique_matches