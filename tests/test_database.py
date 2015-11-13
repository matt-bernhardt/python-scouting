# -*- coding: utf-8 -*-
from __future__ import absolute_import

from lamont.database import Database


def test_database():
    db = Database()
    assert db.cnx == ''
    assert db.cursor == ''


def test_connection():
    db = Database()
    db.connect()
    assert db.cnx == ''  # This should fail
