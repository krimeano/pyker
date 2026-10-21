from pyker.main import main


def test_main_prints_expected_lines(capsys) -> None:
    result = main()
    captured = capsys.readouterr()

    assert result == 0
    assert "lorem" in captured.out
    assert "ipsum dolor" in captured.out
