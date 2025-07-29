# walks the file system based on config.json rules

import os
import json
from pathlib import Path
from typing import List
from ingest.loader import load_file
from ingest.document import Document

def get_config():
    with open('config.json', 'r') as f:
        return json.load(f)
    
def is_valid_file(path: Path, allowed_exts: List[str]) -> bool:
    """
    Check if the file has an allowed extension.
    
    Args:
        path (Path): The file path to check.
        allowed_exts (List[str]): List of allowed file extensions.
    
    Returns:
        bool: True if the file is valid, False otherwise.
    """
    return path.is_file() and path.suffix.lower() in allowed_exts


def crawl_directories() -> List[Document]:
    """
    Crawls directories based on the configuration and returns a list of Document objects.
    
    Returns:
        List[Document]: A list of Document objects loaded from the files.
    """
    config = get_config()
    include_dirs = [Path(p) for p in config.get('include_dirs', [])]
    exclude_patterns = config.get('exclude_patterns', [])
    file_types = config.get('file_types', [])

    collected_docs = []
    for base_dir in include_dirs:
        for root, dirs, files in os.walk(base_dir):
            # Exclude directories based on patterns
            if any(ex in root for ex in exclude_patterns):
                continue
            for file in files:
                path = Path(root) / file
                if is_valid_file(path, file_types):
                    doc = load_file(path)
                    if doc:
                        collected_docs.append(doc)

    return collected_docs