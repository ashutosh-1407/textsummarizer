import os
from box.exceptions import BoxValueError
import yaml
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

from textsummarizer.logging import logger


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    logger.info(f"Reading YAML file: {path_to_yaml}")
    try:
        with open(path_to_yaml, "r") as f:
            content = yaml.safe_load(f)
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty or invalid.")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories: list[Path], verbose: bool = True):
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory: {path}")
        
@ensure_annotations
def get_size(path_to_file: Path):
    size_in_kb = round(os.path.getsize(path_to_file) / 1024)
    return f"~ {size_in_kb} KB"
