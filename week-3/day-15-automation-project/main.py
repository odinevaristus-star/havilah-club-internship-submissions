# Day 15 — Python Automation Project
# Option C: Data Cleaner — removes duplicate rows, strips whitespace, standardises columns
# Submit the complete project (this file + data folder + README.md) to GitHub.

import os
import csv

# ── Configuration ─────────────────────────────────────────────────────────────
# Set your input/output file paths here so they are easy to find and change.

INPUT_FILE = "data/raw_data.csv"
OUTPUT_FILE = "data/output/cleaned_data.csv"


# ── Core Functions ─────────────────────────────────────────────────────────────
def load_data(filepath):
    """Loads CSV rows into a list of dictionaries."""
    rows = []
    try:
        with open(filepath, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                rows.append(dict(row))
        print(f"Successfully loaded {len(rows)} raw rows from '{filepath}'.")
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found. Please ensure raw_data.csv is inside the data/ folder.")
    except Exception as e:
        print(f"An error occurred while loading the file: {e}")
    return rows


def clean_data(rows):
    """Strips whitespace, standardises column headers, and removes duplicate rows."""
    if not rows:
        return []

    cleaned_rows = []
    seen_rows = set()
    initial_count = len(rows)

    for row in rows:
        # 1. Standardise keys (headers): lowercase and replace spaces with underscores
        # 2. Strip whitespace from string values
        cleaned_row = {}
        for key, val in row.items():
            standard_key = key.strip().lower().replace(" ", "_")
            cleaned_val = val.strip() if isinstance(val, str) else val
            cleaned_row[standard_key] = cleaned_val

        # 3. Prevent duplicate rows by converting row dict into a sorted tuple
        row_tuple = tuple(sorted(cleaned_row.items()))
        
        if row_tuple not in seen_rows:
            seen_rows.add(row_tuple)
            cleaned_rows.append(cleaned_row)

    duplicates_removed = initial_count - len(cleaned_rows)
    print(f"Data cleaning complete: Removed {duplicates_removed} duplicate row(s).")
    return cleaned_rows


def save_data(rows, filepath):
    """Ensures output directory exists and writes cleaned rows to a new CSV file."""
    if not rows:
        print("No rows to save.")
        return

    # Automatically create the output folder if it doesn't exist
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    fieldnames = rows[0].keys()

    try:
        with open(filepath, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
        print(f"Successfully exported cleaned data to '{filepath}'.")
    except Exception as e:
        print(f"Error writing to file: {e}")


def process(input_path, output_path):
    """Orchestrates the data cleaning pipeline."""
    rows = load_data(input_path)
    if rows:
        cleaned_rows = clean_data(rows)
        save_data(cleaned_rows, output_path)


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    print("Starting automation pipeline...")
    process(INPUT_FILE, OUTPUT_FILE)
    print("Done.")


if __name__ == "__main__":
    main()