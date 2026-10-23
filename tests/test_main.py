from pyker.main import main


def test_main_prints_expected_lines(capsys, monkeypatch, tmp_path) -> None:
    monkeypatch.setenv("PYKER_CACHE_DIR", str(tmp_path / "cache"))

    result = main()
    captured = capsys.readouterr()

    assert result == 0
    assert "pyker demo" in captured.out
    assert "cached: demo_result" in captured.out
