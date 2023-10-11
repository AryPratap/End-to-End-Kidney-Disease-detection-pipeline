
from dataclasses import dataclass
from pathlib import Path

# Acts as a entity(class as variables can be accessed from other files)
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path