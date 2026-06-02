# P2P Car Rental Experiment

> Reproducible measurement and analysis pipeline for studying marketplace dynamics in peer-to-peer vehicle rental platforms.

This repository contains the code, processed datasets, trained models, and generated plots used for a longitudinal geospatial study of peer-to-peer vehicle rental platforms (PVRPs), including **Turo (TR)**, **Getaround (GA)**, and **Getaround Europe (GE)**.

The project measures how app-mediated vehicle rental marketplaces behave across space and time: what supply is visible, which vehicles are bookable, how prices change, how search rankings reshuffle, and which observable listing signals correlate with utilization.

---

## Study at a Glance

| Item | Summary |
|---|---|
| Platforms | Turo, Getaround, Getaround Europe |
| Scope | 15 cities across 6 countries |
| Measurement window | 200 days, from 2022-10-01 to 2023-04-19 |
| Primary signals | Search results, listing metadata, booking prices, availability, rankings, reviews, host metadata |
| Core analyses | Supply, cross-platform overlap, host portfolios, dynamic pricing, ranking dynamics, inferred utilization |
| Main outputs | Processed datasets, CDFs, heatmaps, ranking models, utilization analysis plots |

---

## Why This Repository Exists

Peer-to-peer vehicle rental platforms are spatial marketplaces: supply, pricing, ranking, and availability are all conditioned on location and time. However, these platforms generally do not provide public fine-grained longitudinal datasets for independent research.

This repository operationalizes a measurement approach that collects renter-visible platform information by tracing and replaying the network requests made by official mobile apps. The resulting data enables independent analysis of:

- how vehicle supply varies across cities and platforms;
- how much overlap exists between platforms operating in the same city;
- whether supply is dominated by one-car hosts or fleet-like hosts;
- how frequently listings update prices;
- how volatile search rankings are over time;
- which public listing features correlate with ranking and utilization.

---

## Repository Layout

```text
.
├── dataCollectionScripts/          # Platform-specific collectors and request replayers
│   ├── Turo/                       # Turo vehicle-list request templates and collector
│   ├── GetAround/                  # Getaround vehicle-list request templates and collector
│   ├── GerAroundEurope/            # Getaround Europe vehicle-list request templates and collector
│   ├── getCarDetails/              # Listing/detail collection scripts
│   ├── getCarReviews/              # Review collection scripts
│   ├── getOwnerDetails/            # Host/owner metadata collection scripts
│   └── GerCarIDs/                  # Utilities for reading and consolidating vehicle IDs
│
├── AnalysisScripts/                # Analysis pipeline scripts used to produce paper results
│   ├── 0-*.py to 8a-*.py           # Raw response parsing, vehicle extraction, supply tables
│   ├── 10*-*.py                    # Vehicle category, color, and supply composition analysis
│   ├── 11*-*.py / 46*-*.py         # Host multiplicity and portfolio analysis
│   ├── 13*-*.py / 33*-*.py         # Booking price and dynamic pricing analysis
│   ├── 14*-*.py / 40*-*.py / 41*-*.py / 42*-*.py
│   │                               # Ranking stability and rank-feature correlation analysis
│   ├── 17*-*.py to 28*-*.py        # Trip, cancellation, utilization, and calendar analyses
│   ├── 43*-*.py                    # XGBoost ranking prediction models
│   ├── 50*-*.py to 64*-*.py        # Owner earnings, distance, advance booking, and demand drivers
│   └── IntermediateData/           # Expected generated intermediate files, if rebuilding from raw data
│
├── Datasets/                       # Processed dictionaries and supporting datasets
│   ├── carCat.txt                  # Raw make/model/category mapping data
│   ├── carCatCleaned.txt           # Cleaned vehicle category mapping
│   ├── carAdvanceBookingHoursDict.txt
│   └── carDatesDict-*.txt          # Per-city availability/date dictionaries
│
├── plots/                          # Paper-ready figures in PNG and EPS formats
├── TurototalData.csv               # Processed rank-model feature table for Turo
├── GetAroundtotalData.csv          # Processed rank-model feature table for Getaround
├── GerAroundEuropetotalData.csv    # Processed rank-model feature table for Getaround Europe
├── *_xgb.pkl                       # Trained XGBoost ranking prediction models
├── runExperiment.py                # Long-running experiment launcher
└── tempFileCreator.py              # Temporary file helper script
```

---

## Measurement Pipeline

The project follows a four-stage workflow.

```mermaid
flowchart LR
    A[Mobile app traffic tracing] --> B[Request template extraction]
    B --> C[Automated request replay]
    C --> D[Timestamped JSON snapshots]
    D --> E[Parsing and normalization]
    E --> F[Supply, price, rank, availability tables]
    F --> G[Marketplace analysis]
    G --> H[Plots, models, and paper figures]
```

### 1. Request discovery

Official app traffic was inspected during normal renter-side interactions, such as searching for vehicles, opening listings, viewing reviews, and checking host profiles. The scripts preserve the resulting endpoint templates, headers, query parameters, and request bodies needed to replay those workflows.

Relevant directories:

```text
dataCollectionScripts/Turo/
dataCollectionScripts/GetAround/
dataCollectionScripts/GerAroundEurope/
```

### 2. Longitudinal collection

The platform-specific `vehicleList.py` scripts issue repeated city/date search requests and store compressed JSON responses. The collection scripts are organized around the main marketplace objects:

| Object | What it captures | Example scripts |
|---|---|---|
| Vehicle list | Ranked search results, visible inventory, quoted prices | `*/vehicleList.py` |
| Vehicle details | Make, model, year, features, policies, descriptions | `getCarDetails/carDetailsRequests.py` |
| Reviews | Review text, review timestamps, listing reputation signals | `getCarReviews/*.py` |
| Host metadata | Host profile and owner-level listing multiplicity | `getOwnerDetails/*.py` |

### 3. Variable inference

The analysis scripts convert raw renter-visible responses into structured variables:

| Variable | Meaning |
|---|---|
| Supply | Unique vehicles visible in a city/platform/window |
| Bookable inventory | Vehicles available for a queried rental window |
| Price | Quoted booking price for a vehicle and rental window |
| Dynamic pricing | Price changes for the same vehicle-window over repeated observations |
| Ranking | Rank position in server-returned search results |
| Host portfolio size | Number of vehicles listed by the same host |
| Trip / cancellation signal | Inferred from availability transitions and platform trip counters |
| Utilization | Average trips per vehicle per month over the observation window |

### 4. Analysis and modeling

The repository includes scripts for generating the paper-level results:

| Topic | Scripts |
|---|---|
| Supply and overlap | `7-overlappingCarsInApps.py`, `8-totalCarsInEachCityByEachProvider.py`, `8a-tableSupply.py` |
| Vehicle categories and colors | `10f-vehicleCategories.py`, `10i-citySuppllyColorAnalysis.py`, `53a-vehicleColorAndDemand.py` |
| Host portfolios | `11a-multiplicity.py`, `11b-multiplicityTableAndAnalysis.py`, `46a-tripsPerOwnerWithXcars.py`, `47a-multiplicityTable.py` |
| Pricing | `33a-bookingPriceAverage.py`, `33h2-cdfDPfrequencyApps.py`, `33m-changePercentageInDP-new.py`, `33o-beforeDaysPricePlot-New.py` |
| Ranking stability | `40a-rankListsOfEachPlatform.py`, `40b-findDiffAndFreqRanking.py`, `40d-drawDiffCDF.py`, `40f-drawAboveFrequencCDF.py` |
| Rank-feature correlations | `41b-ratingAndRanking.py`, `41h-picNumberToRank.py`, `41i-featuresToRank.py`, `41j-wordCountToRank.py`, `42z-drawDivisionPlotRanking.py` |
| Ranking prediction | `43a-predictRankMLmodel.py`, `43b-xgboostPrediction.py` |
| Demand and utilization | `57a-priceAndDemand.py`, `58a-ratingAndDemand.py`, `59a-picCountDemand.py`, `60a-featuresToTrips.py` |

---

## Key Findings Represented by This Repository

The scripts and data support the following high-level results:

1. **Supply is uneven across cities.** A small number of large metropolitan areas dominate observed supply, while several European markets are much smaller.
2. **Cross-platform overlap is low.** In cities where multiple platforms operate, the same vehicles rarely appear on multiple platforms.
3. **One-car hosts are common, but supply is concentrated.** Most hosts list one vehicle, but a small number of multi-vehicle hosts account for a substantial share of inventory.
4. **Dynamic pricing is widespread but platform-dependent.** Price update frequency and update magnitude differ substantially across TR, GA, and GE.
5. **Rankings are stable enough to audit, but not static.** Search results are relatively stable at short timescales and reshuffle over multi-day windows.
6. **Listing quality and trust cues matter.** More complete listings, stronger responsiveness signals, richer review histories, and higher engagement correlate with better ranking and higher utilization.

---

## Quick Start

### 1. Clone the repository

```bash
git clone <repo-url>
cd P2P_Car_Rental_Experiment
```

### 2. Create a Python environment

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

### 3. Install common dependencies

This archive does not currently include a pinned `requirements.txt`. The following package set covers the major analysis scripts:

```bash
pip install \
  pandas numpy scipy matplotlib seaborn requests ujson orjson \
  scikit-learn xgboost rbo deep-translator vaderSentiment \
  wordcloud pillow opencv-python natsort psutil python-dateutil
```

Optional packages used by selected scripts:

```bash
pip install deepface tensorflow keras pydrive gender-guesser pycld2
```

### 4. Inspect processed data

```bash
python - <<'PY'
import pandas as pd

for path in [
    "TurototalData.csv",
    "GetAroundtotalData.csv",
    "GerAroundEuropetotalData.csv",
]:
    df = pd.read_csv(path)
    print(path, df.shape)
    print(df.head())
PY
```

### 5. Open generated plots

Paper-ready plots are available in:

```text
plots/*.png
plots/*.eps
```

Useful starting points:

| Plot | What it shows |
|---|---|
| `plots/7b.png` | Cross-platform vehicle overlap |
| `plots/11b.png` | Host portfolio distribution |
| `plots/33b.png`, `plots/33c.png` | Price distribution summaries |
| `plots/40d.png`, `plots/40f.png` | Ranking reshuffle magnitude and update intervals |
| `plots/57b.png`, `plots/58b.png`, `plots/59b.png`, `plots/60b.png` | Demand and utilization drivers |

---

## Reproducing Analyses

The repository is organized as a research snapshot. Many scripts were originally run in a fixed experiment environment and may expect generated intermediate files under paths such as:

```text
AnalysisScripts/IntermediateData/
/home/hakhan/Google Drive/p2pCarRentalProject/
```

Before full reproduction, update hard-coded paths to your local repository path. A simple approach is to define a project root and replace absolute path prefixes:

```python
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "Datasets"
PLOTS_DIR = PROJECT_ROOT / "plots"
```

Recommended reproduction order:

1. Parse collected vehicle-list responses.
2. Build vehicle, owner, price, rank, and availability dictionaries.
3. Generate supply and overlap tables.
4. Generate pricing and dynamic-pricing summaries.
5. Generate ranking stability summaries.
6. Build rank-feature datasets.
7. Train or reload XGBoost rank prediction models.
8. Generate utilization and demand-driver plots.

A practical script sequence starts with:

```text
AnalysisScripts/0-vehicleListRead.py
AnalysisScripts/1-vehicleDetailsRead.py
AnalysisScripts/2-ownerDetailRead.py
AnalysisScripts/3-reviewDetailRead.py
AnalysisScripts/7-overlappingCarsInApps.py
AnalysisScripts/8a-tableSupply.py
AnalysisScripts/33a-bookingPriceAverage.py
AnalysisScripts/40a-rankListsOfEachPlatform.py
AnalysisScripts/43a-predictRankMLmodel.py
```

Not every script is standalone; several scripts consume outputs written by earlier scripts. When in doubt, inspect the input path variables near the top of each file.

---

## Data Files

### Processed ML feature tables

| File | Description |
|---|---|
| `TurototalData.csv` | Feature table used for Turo ranking prediction |
| `GetAroundtotalData.csv` | Feature table used for Getaround ranking prediction |
| `GerAroundEuropetotalData.csv` | Feature table used for Getaround Europe ranking prediction |

Common feature families include rating, review count, trip count, photo count, vehicle category, owner portfolio size, response metrics, feature count, days listed, and rank bucket.

### Trained models

| File | Description |
|---|---|
| `Turo_xgb.pkl` | Trained XGBoost model for Turo ranking prediction |
| `GetAround_xgb.pkl` | Trained XGBoost model for Getaround ranking prediction |
| `GerAroundEurope_xgb.pkl` | Trained XGBoost model for Getaround Europe ranking prediction |

### Supporting dictionaries

| File | Description |
|---|---|
| `Datasets/carCat.txt` | Raw vehicle make/model/category mapping |
| `Datasets/carCatCleaned.txt` | Cleaned category mapping |
| `Datasets/carAdvanceBookingHoursDict.txt` | Advance booking hour dictionary |
| `Datasets/carDatesDict-*.txt` | Per-city vehicle availability/date dictionaries |

---

## Security and Release Checklist

Before making the repository public, review and clean the following items:

- Remove or rotate any historical OAuth tokens, request headers, API keys, proxy addresses, or machine-specific paths.
- Replace hard-coded absolute paths with configurable relative paths.
- Add a pinned `requirements.txt` or `environment.yml`.
- Add a license file.
- Add a small sample dataset for lightweight testing.
- Add a script-level README or Makefile for reproducing each figure.
- Separate data collection code from analysis code if reviewers only need reproducibility of results.
- Document which files are raw data, intermediate data, and final artifacts.

---

## Ethical Use Notes

This repository is intended for reproducible academic measurement of renter-visible marketplace information. Anyone extending the collectors should:

- comply with applicable laws, institutional review requirements, and platform terms;
- avoid collecting private user information beyond what is necessary for aggregate marketplace analysis;
- use conservative request rates and avoid imposing meaningful load on services;
- publish only aggregated or de-identified results;
- avoid releasing active credentials, tokens, or proxy configurations.

---

## Citation

If this repository supports your research, cite the associated paper:

```bibtex
@inproceedings{shahzad2026pvrp,
  title     = {Measuring Marketplace Dynamics in Peer-to-Peer Vehicle Rental Platforms: A Geospatial Longitudinal Study},
  author    = {},
  booktitle = {Proceedings of ACM SIGSPATIAL},
  year      = {2026},
  note      = {Dataset and code release for peer-to-peer vehicle rental platform measurement}
}
```

---

## Contact

For questions about the dataset, methodology, or analysis pipeline, contact the paper authors or open an issue in the repository after public release.
