import json
import jsonschema
import pytest
from jsonschema import validate, Draft202012Validator
from scdex import SCDEX_JSON_SCHEMA, SCDEX_SCHEMA_REPO_ROOT


examples_path = SCDEX_SCHEMA_REPO_ROOT.joinpath("examples", "full")

def test_schema_is_resolved():
    assert SCDEX_JSON_SCHEMA is not None
    assert isinstance(SCDEX_JSON_SCHEMA, dict)
    assert SCDEX_JSON_SCHEMA['title'] == 'SC-DEX Core Schema'

    assert Draft202012Validator.check_schema(SCDEX_JSON_SCHEMA) is None


@pytest.mark.parametrize("path_to_validate", examples_path.glob("valid/*.json"))
def test_valid_examples(path_to_validate):
    print(f"Checking *VALID* path succeeds: {path_to_validate}")
    with open(path_to_validate, 'r') as f:
        data = f.read()
    data = json.loads(data)
    validate(data, SCDEX_JSON_SCHEMA, cls=Draft202012Validator)


@pytest.mark.parametrize("path_to_validate", examples_path.glob("invalid/*.json"))
def test_invalid_examples(path_to_validate):
    print(f"Checking *INVALID* path returns a ValidationError: {path_to_validate}")
    with open(path_to_validate, 'r') as f:
        data = f.read()
    data = json.loads(data)
    with pytest.raises(jsonschema.exceptions.ValidationError):
        validate(data, SCDEX_JSON_SCHEMA, cls=Draft202012Validator)
