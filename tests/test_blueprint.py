from pathlib import Path

SRC_PATH: Path = Path('../blueprint_project')

def test_src_dir_name():
    assert SRC_PATH.name == 'blueprint_project'
