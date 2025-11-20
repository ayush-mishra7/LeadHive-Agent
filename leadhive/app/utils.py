def clean_text(text: str) -> str:
    """
    Cleans and normalizes text by removing extra whitespace.
    """
    return " ".join(text.strip().split())


def normalize_score(score: float, min_val: float = 0, max_val: float = 1) -> float:
    """
    Normalizes a score into a range of 0–1.
    """
    if score < min_val:
        score = min_val
    if score > max_val:
        score = max_val
    return round((score - min_val) / (max_val - min_val), 2)


def format_section(title: str, content: str) -> str:
    """
    Formats a section for consistent markdown output.
    """
    return f"## {title}\n{content}\n"


def safe_get(d: dict, key: str, default=""):
    """
    Safely retrieves dictionary values.
    """
    return d.get(key, default)
