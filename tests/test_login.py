import pytest

def test_run_behave():
    pytest.main(["--html=reports/report.html", "--self-contained-html", "features/"])
