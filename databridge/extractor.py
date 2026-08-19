import re


def extract_accessions(text):
    # find GEO, BioProject, and SRA accession IDs
    matches = re.findall(
        r"\b(?:GSE|PRJNA|SRP|SRX)\d+\b",
        text,
    )

    # remove duplicates while preserving their original order
    unique_matches = list(dict.fromkeys(matches))
    return unique_matches
