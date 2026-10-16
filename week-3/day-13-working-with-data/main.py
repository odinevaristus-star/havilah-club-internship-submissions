# Day 13 — Working With Data
# Task: Load a CSV, manipulate lists and dicts, clean data, and print a summary.
# Submit this script along with your original CSV and the output CSV.

import csv
import os

INPUT_FILE = "data/sample.csv"
OUTPUT_FILE = "data/output.csv"


# ── Step 1: Load CSV ──────────────────────────────────────────────────────────
# Open the CSV file using csv.DictReader and read each row into a list of dicts.

def load_data(filepath):
    rows = []
    try:
        with open(filepath, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                rows.append(dict(row))
        print(f"Successfully loaded {len(rows)} rows from {filepath}.")
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
    except Exception as e:
        print(f"An error occurred while loading the file: {e}")
    return rows

# ── Step 2: Print Summary ─────────────────────────────────────────────────────
# Print the total number of rows.
# For any numeric column, print the minimum, maximum, and average values.

def print_summary(rows):
    if not rows:
        print("No data available to summarize.\n")
        return
    
    total_rows = len(rows)
    print("\n" + "="*40)
    print("          DATA SUMMARY STATISTICS          ")
    print("="*40)
    print(f"Total number of rows: {total_rows}")
    
    columns = rows[0].keys()
    
    for col in columns:
        numeric_values = []
        for row in rows:
            val = row.get(col, "").strip()
            if val:
                try:
                    # Attempt to parse as float (handles both integers and decimals)
                    numeric_values.append(float(val))
                except ValueError:
                    pass

# ── Step 3: Filter Data ───────────────────────────────────────────────────────
# Return only the rows where a specific column meets a condition.
# Example: score above 70, or price below 50.

def filter_data(rows):
    filtered = []
    for row in rows:
        # Check for common metric columns like 'score' or 'price'
        matched = False
        for key, val in row.items():
            key_lower = key.lower()
            try:
                num = float(val)
                # Example condition: Score >= 70 or Price <= 50
                if 'score' in key_lower and num >= 70:
                    matched = True
                    break
                elif 'price' in key_lower and num <= 50:
                    matched = True
                    break
            except ValueError:
                pass
        
        if matched:
            filtered.append(row)
            
    # Fallback: if no rows matched the specific criteria, keep all rows for demonstration
    if not filtered and rows:
        print("Notice: No rows matched the specific filter criteria (Score >= 70 or Price <= 50). Keeping all rows.")
        filtered = rows
        
    return filtered
# ── Step 4: Sort and Export ───────────────────────────────────────────────────
# Sort the filtered data by one column and write the result to OUTPUT_FILE.

def save_data(rows, filepath):
    if not rows:
        print("No rows to save.")
        return
    
    # Determine a good column to sort by (e.g., 'Score', 'Name', or the first column)
    sort_key = list(rows[0].keys())[0]
    for key in rows[0].keys():
        if any(term in key.lower() for term in ['name', 'title', 'score', 'id']):
            sort_key = key
            break

    # Sort rows safely (handling potential numeric vs string values)
    try:
        sorted_rows = sorted(
            rows, 
            key=lambda x: float(x[sort_key]) if x[sort_key].replace('.', '', 1).isdigit() else str(x[sort_key])
        )
    except Exception:
        sorted_rows = sorted(rows, key=lambda x: str(x[sort_key]))

    # Ensure the output directory exists
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    
    fieldnames = rows[0].keys()
    
    try:
        with open(filepath, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(sorted_rows)
        print(f"Successfully exported sorted data using sort key '{sort_key}'.")
    except Exception as e:
        print(f"Error writing to file: {e}")


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    rows = load_data(INPUT_FILE)
    print_summary(rows)
    filtered = filter_data(rows)
    save_data(filtered, OUTPUT_FILE)
    print(f"Done. {len(filtered)} rows written to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
