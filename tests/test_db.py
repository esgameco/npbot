import pytest
import os

from src import DB

from dotenv import load_dotenv
load_dotenv()

@pytest.mark.asyncio
async def test_db_set():
    db = DB()

    key = 'key'
    value = 'value'

    db.set(key, value)

    assert db._cache[key] == value

@pytest.mark.asyncio
async def test_db_get():
    db = DB()

    key = 'key'
    value = 'value'

    db._cache[key] = value

    assert db.get(key) == db._cache[key]

@pytest.mark.asyncio
async def test_db_update():
    db = DB()

    key = 'key'
    original_value = {'name': 'john'}
    added_value = {'time': '4AM'}
    expected_value = {'name': 'john', 'time': '4AM'}

    db._cache[key] = original_value

    db.update(key, added_value)

    assert db._cache[key] == expected_value

@pytest.mark.asyncio
async def test_db_save_load_db():
    db = DB()

    db.set('name', 't')
    db.save_db_to_file(os.getenv('TEST_DB_LOC'))

    db2 = DB()

    db2.load_db_from_file(os.getenv('TEST_DB_LOC'))

    assert db2.get('name') == 't'