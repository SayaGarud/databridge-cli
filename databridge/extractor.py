import re


def extract_accessions(text):
    matches = re.findall(r"GSE\d+", text)
    return matches