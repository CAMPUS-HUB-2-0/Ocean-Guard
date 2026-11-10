# OceanGuard – Power BI Dashboard Build Guide

## 1. Import data
1. Open Power BI Desktop.
2. Select **Home → Get data → Text/CSV**.
3. Choose `data/processed/oceanguard_cleaned.csv` and select **Load** (or **Transform Data** to inspect types).
4. Confirm date columns are Date and numeric pollution/index fields are numeric.

## 2. Suggested page layout
**Page 1 – Overview**
- Card: total records (`COUNTROWS` of the imported table).
- Bar chart: records by dominant pollution type/category.
- Bar chart: records by country or city, if present.
- Slicer: observation date, if present.

**Page 2 – Pollution indicators**
- Clustered column chart comparing available numeric pollution indicator columns (for example plastic, fishing waste, sewage and oil).
- Table with location, index value, category and dominant type where those fields exist.
- Scatter chart: pollution index versus selected indicator, if both are available.

**Page 3 – Trends and hotspots**
- Line chart: record count by month using a valid observation date.
- Bar chart: locations ranked by average or total index, using a clearly stated aggregation.
- Slicers: country, city, category and date where available.

## 3. Useful starter measures
Replace `OceanGuard` below with the actual table name shown in the Fields pane.
```DAX
Total Records = COUNTROWS(OceanGuard)
Average Index = AVERAGE(OceanGuard[OceanGuard Index Value])
```
Create the Average Index measure only if that exact numeric column exists. Use the actual column names in the supplied CSV.

## 4. Design
Use a consistent ocean-inspired palette, clear titles, readable labels and slicers. Add a small note on the report page identifying the dataset source and limitations. Avoid clutter and avoid implying live monitoring.

## 5. Validate before submission
- Check card totals against the cleaned CSV row count.
- Check category totals and filters.
- Confirm dates sort chronologically.
- Test every slicer and cross-filter.
- Ensure blanks and unknown values are represented honestly.
- Save as `06_Dashboard/OceanGuard_Dashboard.pbix` and add screenshots of the finished pages.

## 6. Report figures versus dataset calculations
The project report separately states 1,248 total reports, 684 plastic-waste reports, 126 oil-pollution reports, 238 marine-impact reports, 157 cleaned locations and 24 high-pollution areas, with category shares of plastic 55%, fishing waste 18%, sewage 12%, oil 10% and other 5%. Label these as **figures stated in the project report** unless you independently verify that the CSV produces the same values. Do not mix these figures with CSV-derived visuals without clear labels.
