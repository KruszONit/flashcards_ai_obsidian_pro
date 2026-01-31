import builtins
import datetime
import os
from io import StringIO

import pytest

from app.models.note_models import Note
from app.notes_reader.notes_loader import MarkdownNotesLoader


@pytest.fixture
def notes_loader():
    return MarkdownNotesLoader(".", ["python", "#pytest"])

@pytest.fixture
def empty_notes_loader():
    return MarkdownNotesLoader(".", [])


@pytest.fixture(scope="session")
def note_docker():
    return """
    # Docker
    
    Multiline Content
    Multiline Content
    
    #docker#pytest #python
    """


@pytest.fixture(scope="session")  # stub
def file_md(note_docker):
    return StringIO(note_docker)


def test_tags_are_normalized():
    tags = ["python", "#pytest", "#python", "Python", "  docker"]

    nl = MarkdownNotesLoader(".", tags)

    assert nl.tags == {"#python", "#pytest", "#docker"}


# TODO consider to add more test cases for tags func
def test_find_tag_in_multiline_note(note_docker, empty_notes_loader):
    found_tags = empty_notes_loader.find_tags(note_docker)
    assert found_tags == {"#docker", "#pytest", "#python"}


def test_check_tags_from_note_with_tags(notes_loader):
    assert notes_loader.check_tags({"#python", "#pytest"})


def test_check_tags_from_note_without_matching_tags(notes_loader):
    assert not notes_loader.check_tags({"#unit_tests", "#docker"})

def test_get_file_list_returns_markdown_files(monkeypatch, notes_loader):
    # given
    def stub_listdir(path):
        return ["file1.md", "file2.txt"]

    monkeypatch.setattr(os, "listdir", stub_listdir)

    # when
    result = notes_loader.get_file_list()
    # then
    assert result == ["file1.md"]

def test_get_file_list_with_no_file(monkeypatch, empty_notes_loader):
    def stub_listdir(path):
        return []

    monkeypatch.setattr(os, "listdir", stub_listdir)

    with pytest.raises(FileNotFoundError):
        _ = empty_notes_loader.get_file_list()

def test_get_file_list_with_no_file_with_md_extensions(monkeypatch, notes_loader):
    def stub_listdir(path):
        return ['file.txt', 'file2.html']

    monkeypatch.setattr(os, "listdir", stub_listdir)

    with pytest.raises(FileNotFoundError):
        _ = notes_loader.get_file_list()

def test_load_file(monkeypatch, file_md, note_docker):
    def fake_open(file, mode='r', encoding=None):
        assert mode == 'r'
        assert encoding == 'utf-8'
        return file_md

    monkeypatch.setattr(builtins, "open", fake_open)

    result = MarkdownNotesLoader.load_file("test.md")
    assert result == note_docker

def test_load_file_non_utf8(monkeypatch):
    def fake_open_raise(*args, **kwargs):
        raise UnicodeDecodeError("utf-8", b"", 0, 1, "invalid start byte")

    monkeypatch.setattr(builtins, "open", fake_open_raise)

    with pytest.raises(UnicodeDecodeError):
        MarkdownNotesLoader.load_file("test.md")

class DummyNoteLoader(MarkdownNotesLoader):
    def get_file_list(self):
        return ["note1.md"]

    def load_file(self, file):
        return """
    # Docker
    
    Multiline Content
    Multiline Content
    
    #docker#pytest #python
    """

    def find_tags(self, content):
        return {"#docker", "#pytest", "#python"}

    def check_tags(self, file_tags):
        return True


def test_load_one_note(monkeypatch):

    fixed_timestamp = 1000000000
    monkeypatch.setattr(os.path, "getmtime", lambda patch: fixed_timestamp)

    loader = DummyNoteLoader("./mock", ["python", "#pytest"])
    notes = loader.load()
    note = notes[0]


    assert len(notes) == 1
    assert note.title == "note1"
    assert note.content == """
    # Docker
    
    Multiline Content
    Multiline Content
    
    #docker#pytest #python
    """
    assert note.tags == {"#docker", "#pytest"}
    assert note.updated_at == datetime.fromtimestamp(fixed_timestamp)


