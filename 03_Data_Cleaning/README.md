# Stage 3 – Data Cleaning

**Owner:** P. Samskruthi (`samskruthiporandla-dotcom`)

## Run
```bash
python -m pip install -r requirements.txt
python 03_Data_Cleaning/clean_data.py --input "data/raw/OceanGuard DMS.csv"
```

The script trims column names/text, removes fully duplicated rows, standardizes blank text as missing, attempts date conversion for date-like columns, and writes a cleaned CSV plus a cleaning summary. Review the summary and check data types before analysis. The raw file is never changed.
