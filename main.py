from src.data_generator import generate_data
from src.data_cleaning import clean_data
from src.analysis import analyze_data
from src.visualization import create_visuals
from src.insights import generate_insights

print("\nRunning Expense Tracker Project...\n")

generate_data()
clean_data()
analyze_data()
create_visuals()
generate_insights()

print("\nProject Completed Successfully!")
