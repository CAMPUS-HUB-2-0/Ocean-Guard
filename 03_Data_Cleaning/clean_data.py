"""Beginner-friendly, repeatable cleaning for the OceanGuard CSV."""
import argparse
from pathlib import Path
import pandas as pd


def main():
    parser = argparse.ArgumentParser(description="Clean the OceanGuard CSV without changing the raw file.")
    parser.add_argument("--input", default="data/raw/OceanGuard DMS.csv", help="Path to original CSV")
    parser.add_argument("--output", default="data/processed/oceanguard_cleaned.csv", help="Cleaned CSV output")
    args = parser.parse_args()

    source = Path(args.input)
    if not source.exists():
        raise SystemExit(f"Input file not found: {source}\nPlace the original CSV in data/raw/ or pass --input.")

    df = pd.read_csv(source)
    original_rows, original_columns = df.shape
    df.columns = [str(c).strip() for c in df.columns]
    df = df.loc[:, ~pd.Index(df.columns).duplicated()]
    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].astype("string").str.strip().replace("", pd.NA)

    duplicate_rows = int(df.duplicated().sum())
    df = df.drop_duplicates().copy()
    date_columns = []
    for col in df.columns:
        if any(word in col.lower() for word in ("date", "time", "timestamp")):
            parsed = pd.to_datetime(df[col], errors="coerce")
            if parsed.notna().any():
                df[col] = parsed
                date_columns.append(col)

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output, index=False)
    summary = [
        "# Cleaning summary", "",
        f"- Input file: `{source}`",
        f"- Original rows: {original_rows}",
        f"- Original columns: {original_columns}",
        f"- Duplicate rows removed: {duplicate_rows}",
        f"- Final rows: {len(df)}",
        f"- Final columns: {len(df.columns)}",
        f"- Date columns parsed: {', '.join(date_columns) if date_columns else 'None detected'}",
        f"- Missing values remaining: {int(df.isna().sum().sum())}",
        f"- Output: `{output}`", "",
        "Review missing values and date parsing before using the data in charts. No rows are imputed."
    ]
    Path("03_Data_Cleaning/cleaning_summary.md").write_text("\n".join(summary), encoding="utf-8")
    print("\n".join(summary))


if __name__ == "__main__":
    main()
