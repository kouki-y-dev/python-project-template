"""Tests for the calc module."""

import pytest

from calc import sum_numbers


class TestSumNumbers:
    """Tests for the sum_numbers function."""

    def test_positive_numbers(self) -> None:
        """Test summing two positive numbers."""
        assert sum_numbers(1, 2) == 3

    def test_negative_numbers(self) -> None:
        """Test summing two negative numbers."""
        assert sum_numbers(-1, -2) == -3

    def test_zero(self) -> None:
        """Test summing with zero."""
        assert sum_numbers(0, 0) == 0

    def test_float_numbers(self) -> None:
        """Test summing floating point numbers."""
        assert sum_numbers(1.5, 2.3) == pytest.approx(3.8)
