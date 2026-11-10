"""Create basic charts only for fields actually present in the cleaned data."""
import argparse
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

CATEGORY_HINTS = ("dominant pollution type", "pollution type", "oceanguard index category", "category", "country", "city")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input", default="data/processed/oceanguard_cleaned.csv")
    p.add_argument("--output-dir", default="05_Data_Visualization/charts")
    a = p.parse_args()
    if not Path(a.input).exists():
        raise SystemExit(f"File not found: {a.input}. Run the cleaning script first.")
    df = pd.read_csv(a.input)
    out = Path(a.output_dir)
    out.mkdir(parents=True, exist_ok=True)
    made = 0
    for col in df.columns:
        if col.strip().lower() in CATEGORY_HINTS and df[col].nunique(dropna=True) > 1:
            counts = df[col].fillna("Missing").value_counts().head(15)
            ax = counts.sort_values().plot(kind="barh", figsize=(9, 5), title=f"Records by {col}")
            ax.set_xlabel("Number of records")
            ax.set_ylabel(col)
            plt.tight_layout()
            plt.savefig(out / f"{made+1}_{col.lower().replace(' ', '_')}.png", dpi=160)
            plt.close()
            made += 1
    numeric = df.select_dtypes(include="number")
    if numeric.shape[1] >= 2:
        fig, ax = plt.subplots(figsize=(9, 7))
        image = ax.imshow(numeric.corr(), aspect="auto")
        ax.set_xticks(range(len(numeric.columns)), numeric.columns, rotation=90)
        ax.set_yticks(range(len(numeric.columns)), numeric.columns)
        ax.set_title("Correlation between numeric fields")
        fig.colorbar(image, ax=ax)
        fig.tight_layout()
        fig.savefig(out / "numeric_correlation.png", dpi=160)
        plt.close(fig)
        made += 1
    print(f"Created {made} chart(s) in {out}. If zero, inspect the dataset columns and update field selection.")

if __name__ == "__main__":
    main()
