#!/usr/bin/env python

"""Tests for `sl_forecast` package."""

import pytest


class TestSLForecast:
    """Tests for `sl_forecast` package."""

    @pytest.fixture
    def test_version(self):
        from sl_forecast import __version__

        assert __version__ is not None
