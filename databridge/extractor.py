import re


def extract_accessions(text):
    matches = re.findall(r"GSE\d+", text)

    # remove duplicates while preserving their original order
    unique_matches = list(dict.fromkeys(matches))

    return unique_matches