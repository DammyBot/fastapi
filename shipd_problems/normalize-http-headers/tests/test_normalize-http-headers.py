import pytest

from shipd_problems.normalize_http_headers.solution.impl import normalize_http_headers


def test_examples_case_1():
    headers = [("Content-Type", " text/html "), ("content-type", "charset=utf-8")]
    assert normalize_http_headers(headers) == {"content-type": "text/html, charset=utf-8"}


def test_examples_case_2():
    headers = [("X-Custom", "a"), ("X-Custom", "b "), ("x-custom", "c")]
    assert normalize_http_headers(headers) == {"x-custom": "a, b, c"}


def test_empty_list_returns_empty_dict():
    assert normalize_http_headers([]) == {}


def test_single_header_lowercased_and_trimmed():
    headers = [("  Accept  ", "  application/json  ")]
    assert normalize_http_headers(headers) == {"accept": "application/json"}


def test_duplicate_names_different_cases_and_whitespace_values():
    headers = [("ETag", " abc "), ("etag", ""), ("ETAG", None), ("eTaG", "  def")]
    # Values become ["abc", "", "", "def"], joined in order
    assert normalize_http_headers(headers) == {"etag": "abc, , , def"}


def test_multiple_distinct_headers():
    headers = [("X-A", "1"), ("X-B", " 2 "), ("x-a", "3"), ("X-C", None)]
    result = normalize_http_headers(headers)
    assert result == {"x-a": "1, 3", "x-b": "2", "x-c": ""}
    # Ensure determinism for same inputs
    assert normalize_http_headers(headers) == result
