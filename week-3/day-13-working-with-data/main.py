# Day 13 — Working With Data
# Task: Load a CSV, manipulate lists and dicts, clean data, and print a summary.
# Submit this script along with your original CSV and the output CSV.

import csv

INPUT_FILE = "week-3/day-13-working-with-data/data/sample.csv"
OUTPUT_FILE = "week-3/day-13-working-with-data/data/output.csv"


# ── Step 1: Load CSV ──────────────────────────────────────────────────────────
# Open the CSV file using csv.DictReader and read each row into a list of dicts.

def load_data(filepath):
    rows = []
    try:
        with open(filepath, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Clean whitespace from dictionary keys and values
                cleaned_row = {k.strip(): v.strip() for k, v in row.items()}
                
                # Convert 'score' to float for calculations
                if "score" in cleaned_row:
                    try:
                        cleaned_row["score"] = float(cleaned_row["score"])
                    except ValueError:
                        cleaned_row["score"] = 0.0
                        
                rows.append(cleaned_row)
    except FileNotFoundError:
        print(f"Error: {filepath} not found.")
    return rows


# ── Step 2: Print Summary ─────────────────────────────────────────────────────
# Print the total number of rows.
# For any numeric column, print the minimum, maximum, and average values.

def print_summary(rows):
    total_rows = len(rows)
    print(f"\n=== Dataset Summary ===")
    print(f"Total Records: {total_rows}")
    
    if total_rows == 0:
        return

    # Extract scores
    scores = [row["score"] for row in rows if isinstance(row.get("score"), (int, float))]
    
    if scores:
        print(f"Score Statistics:")
        print(f"  - Minimum Score: {min(scores)}")
        print(f"  - Maximum Score: {max(scores)}")
        print(f"  - Average Score: {sum(scores) / len(scores):.2f}")
    print()


# ── Step 3: Filter Data ───────────────────────────────────────────────────────
# Return only the rows where a specific column meets a condition.
# Example: score above or equal to 70.

def filter_data(rows):
    filtered = []
    for row in rows:
        if row.get("score", 0) >= 70:
            filtered.append(row)
    return filtered


# ── Step 4: Sort and Export ───────────────────────────────────────────────────
# Sort the filtered data by one column and write the result to OUTPUT_FILE.

def save_data(rows, filepath):
    if not rows:
        print("No rows to save.")
        return

    # Sort rows by 'score' in descending order
    sorted_rows = sorted(rows, key=lambda x: x.get("score", 0), reverse=True)
    
    fieldnames = rows[0].keys()
    
    with open(filepath, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(sorted_rows)


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    rows = load_data(INPUT_FILE)
    print_summary(rows)
    filtered = filter_data(rows)
    save_data(filtered, OUTPUT_FILE)
    print(f"Done. {len(filtered)} rows written to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()