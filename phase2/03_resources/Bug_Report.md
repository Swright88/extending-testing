Bug 1.1

## Summary

Removal of special characters in filename

## Description

When using the document_updater.py on a file that has a hypenated name as the title and is being moved from the originals to the finals directory, the hypen is removed from the filename. This is unexpected behaviour as the filename should remain the same for traceability + database purposes.

## Steps to Reproduce

1. Create a file with a hypenated name (e.g. Cooper-Jones) in 'Originals'
2. Add the Surname to the 'allowlist'
3. Run the 'document_updater.py' program

## Expected Result

Filename is not modified

## Actual Result

Filename was modified

