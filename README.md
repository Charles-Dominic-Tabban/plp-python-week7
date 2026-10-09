# PLP Python Week 7 - Shopping List Manager

## Files

- `list_warmup.py` - Practises list indexing, negative indexing, len(), append(), and remove().
- `shopping_list.py` - Provides a menu to view, add, and remove shopping items.
- `list_report.py` - Counts items with more than four letters and finds the longest item using a manual loop.

## Why is checking membership before deletion safer?

Checking whether an item is in the list before calling `remove()` prevents a `ValueError` if the item does not exist. This makes the program more reliable and helps it continue running without crashing.