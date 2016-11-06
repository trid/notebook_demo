import os
import pytest

from backend.data_storage import DataStorage


@pytest.fixture
def storage():
    ds = DataStorage()
    ds.create_item("John", "Smith", "+1111111111", "05.11.1955")
    ds.create_item("John", "Doe", "+122222222", "14.11.1970")
    ds.create_item("Maria", "Hanasaku", "+1333333333", "11.11.1911")
    ds.create_item("David", "Iroha", "+1444444444", "08.11.1855")
    return ds


@pytest.fixture
def saved_storage():
    ds = DataStorage()
    ds.create_item("John", "Smith", "+1111111111", "05.11.1955")
    ds.create_item("John", "Doe", "+122222222", "14.11.1970")
    ds.create_item("Maria", "Hanasaku", "+1333333333", "11.11.1911")
    ds.create_item("David", "Iroha", "+1444444444", "08.11.1855")
    ds.save("tmp.db")
    yield ds
    os.remove("tmp.db")


def test_add_one_item():
    ds = DataStorage()
    ds.create_item("John", "Smith", "+1111111111", "05.11.2016")
    items = ds.items
    assert len(items) == 1
    assert items[0].first_name == "John" and items[0].last_name == "Smith"


def test_add_few_items():
    ds = DataStorage()
    ds.create_item("John", "First", "+1111111111", "05.11.2016")
    ds.create_item("John", "Second", "+1111111111", "05.11.2016")
    ds.create_item("John", "Third", "+1111111111", "05.11.2016")
    items = ds.items
    assert len(items) == 3
    assert items[0].last_name == "First" and items[1].last_name == "Second" and items[2].last_name == "Third"


def test_save_stored_data(storage):
    storage.save(":memory:")
    assert storage.filename == ":memory:"
    assert storage.items[0].id is not None


def test_update_stored_data(saved_storage):
    old_id = saved_storage.items[0].id
    saved_storage.items[0].last_name = "Holy"
    saved_storage.save()
    assert saved_storage.items[0].id == old_id


def test_load_stored_data(saved_storage):
    loaded_storage = DataStorage(saved_storage.filename)
    assert len(loaded_storage.items) == len(saved_storage.items)
    for i in range(len(loaded_storage.items)):
        assert saved_storage.items[i] == loaded_storage.items[i]


def test_delete_data(storage):
    storage.delete_item(1)
    assert len(storage.items) == 3


def test_delete_and_save_data(saved_storage):
    saved_storage.delete_item(1)
    saved_storage.save()
    loaded_storage = DataStorage(saved_storage.filename)
    assert len(loaded_storage.items) == len(saved_storage.items)
    for i in range(len(loaded_storage.items)):
        assert saved_storage.items[i] == loaded_storage.items[i]