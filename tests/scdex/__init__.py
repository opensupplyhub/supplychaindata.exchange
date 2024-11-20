"""
This module simply exposes the SCDEX JSON schema as a Python constant for use in testing.
It also provides a JSON schema validator with reference resolution, configured to work with the SCDEX core schema and its dependencies.
"""
from pathlib import Path
import json

from jsonschema import Draft202012Validator, RefResolver

SCDEX_SCHEMA_REPO_ROOT =  Path(__file__).parent.parent.parent

with open(SCDEX_SCHEMA_REPO_ROOT.joinpath("schema", "core-schema.json"), 'r') as f:
    _schema_content = f.read()

SCDEX_JSON_SCHEMA = json.loads(_schema_content)

resolver = RefResolver(
    base_uri=f'{SCDEX_SCHEMA_REPO_ROOT.joinpath("schema").resolve().as_uri()}/',  # base directory for schema files
    referrer=SCDEX_JSON_SCHEMA
)

validator = Draft202012Validator(schema=SCDEX_JSON_SCHEMA, resolver=resolver)