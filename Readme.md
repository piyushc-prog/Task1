# Fair Price Shop (PDS) Data Analysis & Feature Engineering

## Project Overview
This project performs data cleaning, analysis, and feature engineering on a dataset containing transaction and commodity distribution details of Fair Price Shops (FPS) across districts for the year 2018.

The goal is to clean the dataset, identify anomalies, generate new analytical features, and produce district-level insights.

---

## Technologies Used
- Python
- Pandas
- NumPy
- Jupyter Notebook

---

## Project Tasks

### 1. Data Loading & Exploration
- Loaded dataset using pandas
- Inspected data using head(), info(), describe()
- Checked for missing values and replaced numeric NaN values with 0

### 2. Data Cleaning
- Removed shops with 0 ration cards but having transactions
- Converted negative totalAmount values to absolute
- Created overflow flag for cases where transactions exceed ration cards

### 3. Feature Engineering
Created new analytical features:
- **total_rice** → Sum of riceAfsc, riceFsc, riceAap
- **total_volume** → Total distributed commodities
- **trans_rate** → Transaction rate percentage
- **shop_category** → Shop performance classification

### 4. Aggregation & Grouping
Generated district-level insights:
- Total revenue per district
- Average transactions per shop
- Total commodities distributed

### 5. Final Output
- Removed redundant rice columns
- Exported cleaned dataset to `engineered_shop_data.csv`

---

## Output
The final cleaned and feature-engineered dataset is saved as:


## Made a virtual Env
py -3.11 -m venv name_venv   
# activate it
.\name_venv\Scripts\activate
# now install packages
pip install numpy pandas jupyter ipykernel


##
Run the notebook:


jupyter notebook


Open the `main.ipynb` file and execute all cells.

