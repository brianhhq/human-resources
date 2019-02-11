import pytest

from hr import cli

@pytest.fixture()
def parser():
    return cli.create_parser()

def test_parser_without_driver():
    """
    Without a specified driver the parser will exit
    """
    with pytest.raises(SystemExit):
        parser.parse_args()
