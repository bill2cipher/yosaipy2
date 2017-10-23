#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .compat import py3k


class NoValue(object):
    """Describe a missing cache value.

    The :attr:`.NO_VALUE` module global
    should be used.

    """

    @property
    def payload(self):
        return self

    def __repr__(self):
        """Ensure __repr__ is a consistent value in case NoValue is used to
        fill another cache key.

        """
        return '<dogpile.cache.api.NoValue object>'

    if py3k:
        def __bool__(self):  # pragma NO COVERAGE
            return False
    else:
        def __nonzero__(self):  # pragma NO COVERAGE
            return False


NO_VALUE = NoValue()
