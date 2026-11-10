"""Exploratory analysis that adapts to the columns in the supplied CSV."""
import argparse
from pathlib import Path
import pandas as pd

CANDIDATES = ("country", "city", "dominant pollution type", "pollution type", "oceanguard index category", "category", "data status")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input", default="data/processed/oceanguard_cleaned.csv")
    p.add_argument("--output", default="04_Data_Analysis/analysis_summary.md")
    a = p.parse_args()
    path = Path(a.input)
    if not path.exists():
        raise SystemExit(f"File not found: {path}. Run the cleaning script first.")
    df = pd.read_csv(path)
    lines = ["# OceanGuard – Exploratory Data Analysis", "", f"- Rows: {len(df)}", f"- Columns: {len(df.columns)}", f"- Duplicate rows: {int(df.duplicated().sum())}", f"- Total missing cells: {int(df.isna().sum().sum())}", "", "## Columns", ""]
    lines += [f"- `{c}` ({df[c].dtype}); missing: {int(df[c].isna().sum())}" for c in df.columns]
    numeric = df.select_dtypes(include="number")
    if not numeric.empty:
        lines += ["", "## Numeric summary", "", numeric.describe().round(2).to_markdown()]
    for col in df.columns:
        if col.strip().lower() in CANDIDATES:
            lines += ["", f"## Frequency: {col}", "", df[col].value_counts(dropna=False).head(20).to_markdown()]
    lines += ["", "## Interpretation reminder", "", "Describe only patterns visible in this dataset. Counts are records, not necessarily unique incidents. Do not infer causation or claim global coverage without evidence."]
    Path(a.output).parent.mkdir(parents=True, exist_ok=True)
    Path(a.output).write_text("\n".join(lines), encoding="utf-8")
    print(f"Analysis written to {a.output}")

if __name__ == "__main__":
    main()
