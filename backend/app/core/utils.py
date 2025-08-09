import re

def clean_text(text: str) -> str:
    """Clean text by removing extra whitespace and normalizing."""
    text = re.sub(r'\s+', ' ', text).strip()
    return text