#!/usr/bin/env python

"""Tests for `sl_forecast` package."""


class TestSLForecast(object):
    """Tests for `sl_forecast` package."""

    def setup_method(self):
        """Setup test fixtures, if any."""
        pass

    def test_version(self):
        from sl_forecast import __version__

        assert __version__ is not None
