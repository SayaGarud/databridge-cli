from databridge.extractor import extract_accessions


def test_extract_gse_accessions():
    text = "We used GEO datasets GSE123456 and GSE789012."

    result = extract_accessions(text)

    assert result == ["GSE123456", "GSE789012"]