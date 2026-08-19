from databridge.extractor import extract_accessions


def test_extract_gse_accessions():
    # example publication text containing two GEO accessions
    text = "We used GEO datasets GSE123456 and GSE789012."

    # run the accession extractor
    result = extract_accessions(text)

    # check that the extracted accessions match 
    assert result == ["GSE123456", "GSE789012"]


def test_extract_accessions_empty_text():
    # empty text should return an empty list
    result = extract_accessions("")

    # verify that no accessions were found
    assert result == []