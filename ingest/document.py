from dataclasses import dataclass
from pathlib import Path
from typing import Optional

@dataclass
class Document:
    """
    Represents a document with its metadata.

    Attributes:
        TO DO
    """
    content: str
    source_path: Path
    file_type: str
    metadata: Optional[dict] = None