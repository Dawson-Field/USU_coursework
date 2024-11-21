# Cryptocurrency Exchange Trading - Arbitrage Detection

## Overview
This program aims to explore cryptocurrency exchange rates using graph traversal techniques. The task is to detect potential arbitrage opportunities by analyzing cryptocurrency exchange rates between different cryptocurrencies (e.g., Bitcoin, Ethereum, Litecoin). The project involves using graph data structures to represent cryptocurrency pairs and their exchange rates, calculating possible paths that maximize the trade value, and detecting "dis-equilibrium" which indicates arbitrage opportunities.

The program will fetch real-time exchange rates from the CoinGecko API and use the NetworkX library to build a directed graph. It will then calculate and compare the exchange rates along different paths between cryptocurrency nodes to detect any discrepancies in pricing, which can be leveraged for profit.

## Requirements
- **Python 3.x**
- **NetworkX** - library for graph creation and traversal
- **requests** - library for fetching real-time data from the CoinGecko API

## Libraries:
To install the necessary libraries, run the following command in a terminal:
```bash
python3 -m pip install networkx requests
```

## How it Works
1. **Data Fetching:**
    - The program fetches the most recent cryptocurrency exchange rates from the CoinGecko API using the /simple/price endpoint.
    - Example URL: https://api.coingecko.com/api/v3/simple/price?ids=ethereum,bitcoin&vs_currencies=eth,btc
    - This returns the exchange rates between different cryptocurrency pairs (e.g., Bitcoin to Ethereum, Ethereum to Bitcoin).
2. **Graph Construction:**
    - The program uses the NetworkX library to construct a directed graph where each cryptocurrency (e.g., BTC, ETH LTC) is a node.
    - The exchange rates between the currencies form the edges between the nodes.

3. **Graph Traversal and Arbitrage Detection:**
    - The program calculates all paths from one currency to another, evaluating the "weight" (exchange rate) of each path by multiplying the weights of the edges in the path.
    - It checks for arbitrage opportunities by comparing paths between two currencies in both directions.
    - If the product of the weights of both paths deviates from 1.0, it indicates a dis-equilibrium, and thus an arbitrage opportunity.
4. **Output:**
    - The program outputs all paths between currency pairs along with their calculated weight and path weight factor.
    - It also identifies the smallest and largest path weight factors to highlight the best arbitrage opportunities.

## Data Sources
The program fetches cryptocurrency data from the CoinGecko API. The API provides real-time pricing information, which is parsed and used to build the graph structure. The API query is configured to pull prices for the following top 7 cryptocurrencies:

- Bitcoin (BTC)
- Ethereum (ETH)
- Ripple (XRP)
- Cardano (ADA)
- Bitcoin Cash (BCH)
- EOS (EOS)
- Litecoin (LTC)

## Code Structure
- **arbitrage.py**: Main script that handles fetching data from the API, constructing the graph, performing the graph traversal, and printing the output.
- **crypto_exchange_graph.png**: A png showing cryptocurrency exchange rates between different cryptocurrencies.
- **exchange_rates.json**: A JSON file containing real-time cryptocurrency exchange rates between various cryptocurrencies
- **README.md**: This file, provides an overview of the project.

## Contact
For any questions or feedback, feel free to contact me at [dawsontfield@gmail.com](mailto:dawsontfield@gmail.com).
