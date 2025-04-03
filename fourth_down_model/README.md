# Fourth Down Decision Model

This project analyzes NFL teams' fourth down decision-making tendencies and categorizes teams into three distinct styles: aggressive, balanced, or conservative. The model uses historical NFL play-by-play data to understand what factors most influence teams' fourth down decisions and how these decisions vary across different teams.

> **Note**: This project originated as a class assignment and has been significantly improved. You can view the enhanced version with additional features on a different repo at [NFL Fourth Down Model](https://github.com/Dawson-Field/nfl-4th-down-decision-model).

## Project Structure

```
fourth_down_model/
├── data/
│   ├── train_data.csv      # Training dataset
│   ├── test_data.csv       # Test dataset
│   ├── team_compliance.csv # Team compliance data
│   └── full_data.csv       # Complete dataset
├── fourth_down_model.ipynb # Main Jupyter notebook
└── results.json            # Model results and predictions
```

## Requirements

The project requires the following Python packages:
- tensorflow
- pycaret
- pandas
- scikit-learn
- nfl_data_py
- matplotlib

## Data

The model uses NFL play-by-play data from the `nfl_data_py` package, which provides comprehensive statistics and play information. The data is processed to focus on fourth down situations and team-specific decision patterns.

## Analysis Features

The model analyzes various factors that influence fourth down decisions, including:
- Score differential
- Time remaining
- Field position
- Yards to go
- Timeouts remaining


## Team Categorization

Teams are categorized into three distinct styles based on their fourth down decision patterns:

1. **Aggressive**: Teams that frequently go for it on fourth down, prioritizing maintaining possession
2. **Balanced**: Teams that make decisions based on traditional analytics and game situation
3. **Conservative**: Teams that tend to punt or kick field goals more often on fourth down

## Usage

1. Install the required dependencies:
```bash
pip install tensorflow pycaret pandas scikit-learn nfl_data_py matplotlib
```

2. Run the Jupyter notebook `fourth_down_model.ipynb` to:
   - Load and preprocess the data
   - Perform feature importance analysis
   - Categorize teams into decision-making styles
   - Generate visualizations of team tendencies

## Results

Model results and predictions are stored in `results.json`, which includes:
- Feature importance rankings
- Team categorization results
- Decision-making patterns by team
- Key insights and recommendations

## Future Improvements

- Incorporate real-time game data
- Add more advanced features (player-specific statistics, injury data)
- Implement a web interface for easy access to team categorizations
- Expand analysis to include other critical game decisions
- Add historical trend analysis of team decision-making styles
