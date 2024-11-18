#!/usr/bin/env python

"""Tests for `sl_forecast` package."""

import pytest


class TestSLForecast:
    """Tests for `sl_forecast` package."""

    def setup_class(cls):
        """Setup test fixtures, if any."""
        pass

    def test_version(self):
        from sl_forecast import __version__

        assert __version__ is not None

    def teardown_class(cls):
        """Teardown test fixtures, if any."""
        pass
