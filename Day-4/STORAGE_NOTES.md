# Day 3 — Persistence and Data Integrity

## Storage implementation

The Contact Manager uses a JSON-backed repository to store contacts. The repository is isolated behind a `ContactRepository` interface, allowing the storage implementation to be replaced with a database later.

## Data integrity

- Contact records are explicitly serialized using `Contact.to_dict()` and reconstructed using `Contact.from_dict()`.
- Missing files are treated as an empty collection.
- Empty files and malformed JSON produce controlled errors.
- Unexpected record shapes and duplicate contact IDs are rejected.
- Contact records are returned in deterministic contact-ID order.
- File updates use a temporary file and `os.replace()` to reduce the risk of partial writes.

## Recovery behavior

A missing data file is safe to initialize. An empty or corrupted file is not automatically overwritten; the application raises an error so the original data can be inspected and recovered.

Recovery procedure:

1. Stop the application.
2. Make a backup copy of `contacts.json`.
3. Inspect or restore the file from a valid backup.
4. Run the application again and verify the records.

## Limitations of JSON storage

- JSON files are suitable for small, single-user projects.
- Concurrent writes from multiple application processes are not coordinated.
- There are no database transactions, indexes, or built-in access controls.
- Atomic replacement reduces the risk of incomplete writes but does not guarantee recovery from all hardware or filesystem failures.

## Future database replacement

The service layer depends on the `ContactRepository` interface rather than JSON-specific file operations. A future database repository can implement the same methods, allowing the CLI and service logic to remain mostly unchanged.
