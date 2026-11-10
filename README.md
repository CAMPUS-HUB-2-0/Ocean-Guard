# OceanGuard – Cleaner Seas, Healthier Future

A human-centered Data Analytics and Visualization project for sea-pollution monitoring and awareness.

## Project overview
OceanGuard brings pollution reporting, location mapping, waste classification, analytics, hotspot identification, awareness and cleanup activities into one proposed platform. It is intended to help students, beach visitors, fishermen, local communities, NGOs, researchers and authorities understand pollution patterns and support cleanup decisions.

## Project workflow
1. Project Proposal
2. Data Collection
3. Data Cleaning
4. Data Analysis
5. Data Visualization
6. Interactive Dashboard (Power BI)

## Repository structure
Each numbered folder documents one project stage. See the folder README files for tasks and deliverables.

## Data and interpretation
Use the team's supplied CSV as the source for analysis. The project report separately states illustrative dashboard figures (1,248 total reports; 684 plastic-waste reports; 126 oil-pollution reports; 238 marine-impact reports; 157 cleaned locations; 24 high-pollution areas). These are report-provided figures and must not be represented as calculations from the CSV unless verified against it. Do not present coursework/synthetic data as live or independently verified ocean measurements.

## Power BI dashboard
The dashboard is a deliverable to be built in Power BI Desktop. This repository currently contains the dashboard specification and build guide; a `.pbix` file should be added only after the team creates and tests the actual report.

## Team responsibilities
- **ashrithbabu – Ashrith Babu:** Project Proposal and Data Collection (Stages 1–2)
- **vinaybabusamala15-max – Vinay Babu Samala:** Data Analytics and Data Visualization (Stages 4–5)
- **samskruthiporandla-dotcom – P. Samskruthi:** Data Cleaning and Interactive Dashboard (Stages 3 and 6)

## Getting started
1. Place the original dataset in `data/raw/` without changing it.
2. Install dependencies: `pip install -r requirements.txt`.
3. Run `python 03_Data_Cleaning/clean_data.py --input "data/raw/OceanGuard DMS.csv"`.
4. Run analysis and visualization scripts using the cleaned CSV; see their folder guides.
5. Import the cleaned CSV into Power BI Desktop and follow `06_Dashboard/powerbi_dashboard_guide.md`.

## Important note
The dashboard and analyses are coursework outputs. Record the dataset source, cleaning decisions, filters and limitations clearly. Do not invent measurements or claim that a feature is deployed when it is only proposed.
