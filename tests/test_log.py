# -*- coding: utf-8 -*-
from __future__ import absolute_import

from lamont.log import Log


def test_log_filename():
    l = Log('test.log')
    assert l.name == 'test.log'
