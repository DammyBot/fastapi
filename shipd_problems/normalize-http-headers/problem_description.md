Title: normalize_http_headers

Description:
Implement 
normalize_http_headers(headers: list[tuple[str, str]]) -> dict[str, str].

Rules:
Input: a list of (name, value) pairs where 
ame and value are strings; value may be None.
The function returns a dict mapping canonical header names to single string values.
Canonicalization: header names are normalized to lowercase and trimmed of surrounding whitespace.
Duplicate header names (case-insensitive) are combined: values are trimmed and then concatenated in *input order* with ", " (comma+space) between entries.
None values are treated as empty string "".
Leading/trailing whitespace of values is trimmed before merging.
The function must be deterministic and not depend on system state.

Examples:
Input: [("Content-Type"," text/html "), ("content-type","charset=utf-8")]
Output: {"content-type": "text/html, charset=utf-8"}

Input: [("X-Custom","a"), ("X-Custom","b "), ("x-custom","c")]
Output: {"x-custom": "a, b, c"}

Edge cases to test:
Empty list -> empty dict
Single header
Duplicate names with differing cases
Values which are empty string, whitespace only, or None
Multiple distinct headers

Acceptance criteria (tests must validate all):
canonical names are lowercase
order of merged values matches input order
trimming of whitespace and conversion of None to ""
deterministic output for same inputs
