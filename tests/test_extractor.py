from databridge.extractor import extract_accessions


def test_extract_gse_accessions():
    text = "We used GEO datasets GSE123456 and GSE789012."
    result = extract_accessions(text)
    assert result == ["GSE123456", "GSE789012"]


def test_extract_accessions_empty_text():
    result = extract_accessions("")
    assert result == []

def test_extract_unique_accessions():
    text = "GSE123456 was used. We analyzed GSE789012 and GSE123456 again."
    result = extract_accessions(text)
    assert result == ["GSE123456", "GSE789012"]

def test_extract_sra_accessions():
    text = "The study SRP123456 contains sequencing experiment SRX789012."
    result = extract_accessions(text)
    assert result == ["SRP123456", "SRX789012"]