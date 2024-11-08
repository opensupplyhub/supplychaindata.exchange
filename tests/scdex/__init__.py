"""
This module simply exposes the SCDEX JSON schema as a Python constant for use in testing.
"""
from pathlib import Path
import json

SCDEX_SCHEMA_REPO_ROOT =  Path(__file__).parent.parent.parent

with open(SCDEX_SCHEMA_REPO_ROOT.joinpath("schema", "core-schema.json"), 'r') as f:
    _schema_content = f.read()

SCDEX_JSON_SCHEMA = json.loads(_schema_content)
