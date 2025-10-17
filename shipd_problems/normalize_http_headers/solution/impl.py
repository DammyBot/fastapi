from typing import Iterable, List, Tuple, Dict, Optional


def normalize_http_headers(headers: List[Tuple[str, Optional[str]]]) -> Dict[str, str]:
    canonical_to_values: Dict[str, List[str]] = {}
    for name, value in headers:
        canonical = (name or "").strip().lower()
        # Treat None as empty string, then trim whitespace
        normalized_value = ("" if value is None else value).strip()
        if canonical not in canonical_to_values:
            canonical_to_values[canonical] = []
        canonical_to_values[canonical].append(normalized_value)
    # Join values in input order with ', '
    return {k: ", ".join(vs) for k, vs in canonical_to_values.items() if k != "" or vs}
