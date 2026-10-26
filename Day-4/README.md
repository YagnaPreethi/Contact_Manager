## Day 4 — Automated Testing and Quality Gates

### Testing Framework

The project uses pytest for automated testing. Existing unittest-based tests are also supported by pytest.

### Install pytest

```bash
python -m pip install pytest
```

### Run the complete test suite

Run the following command from the project root:

```bash
python -m pytest -v
```

**Expected outcome:** All discovered tests pass. The final pytest summary displays the actual number of passed, failed, and skipped tests.

### Run individual test modules

```bash
python -m pytest -v test_day2.py
python -m pytest -v test_day3.py
python -m pytest -v test_models.py
python -m pytest -v test_services.py
```

### Check Python syntax

```bash
python -m compileall -q contact_app run.py
```

**Expected outcome:** The command completes without reporting syntax errors.

### Test Coverage

The automated test suite covers:

- Contact creation and model validation
- Contact serialization and deserialization
- Service-layer create, list, retrieve, update, and delete operations
- Missing IDs and invalid input values
- Duplicate phone numbers and contact IDs
- Missing files, empty files, and malformed JSON
- Invalid records and update/delete edge cases
- Persistence across repository reloads
- Deterministic ordering of stored contacts

### Test Data Isolation

Tests use temporary directories and files so they do not modify the application's real `contacts.json` file.

### Optional Quality Tools

Python compilation checks are available through the standard library. Ruff or another formatter/linter may be used if installed. Optional tools are not required for the core test suite.

### Completion Criteria

The Day 4 task is complete when the full test suite runs successfully, test data is isolated, the README documents the exact commands, and the test report reflects the actual execution results.