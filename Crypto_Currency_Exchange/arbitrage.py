import os
import requests
import json
import networkx as nx
import itertools
import matplotlib.pyplot as plt

# Define cryptocurrencies and their API ids and ticker symbols
coins = {
    'bitcoin': 'btc',
    'ethereum': 'eth',
    'ripple': 'xrp',
    'cardano': 'ada',
    'bitcoin-cash': 'bch',
    'eos': 'eos',
    'litecoin': 'ltc'
}

def get_exchange_rates():
    
# Fetch exchange rates with the API and save the data to a JSON file

    # Construct API URL
    ids = ','.join(coins.keys())
    vs_currencies = ','.join(coins.values())
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={ids}&vs_currencies={vs_currencies}'
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise for bad responses
        
        data = response.json()
        
        # Get the directory of the current script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Construct the path to save the JSON file in the same directory
        json_path = os.path.join(script_dir, "exchange_rates.json")
        
        # Save the JSON response to the file
        with open(json_path, "w") as json_file:
            json.dump(data, json_file, indent=4)
        
        print(f"Exchange rates successfully saved to {json_path}")
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching exchange rates: {e}")
    except json.JSONDecodeError:
        print("Error decoding JSON response.")
    return {}


def build_graph(data):
 
# Build a graph from exchange rate data.

    g = nx.DiGraph()

    # add edges to the graph based on the fetch cxchange rates
    for coin, coin_data in data.items():
        for ticker, rate in coin_data.items():
            node_from = coins.get(coin)
            node_to = ticker
            if node_from and node_to:
                g.add_edge(node_from, node_to, weight=rate)
            else:
                print(f"Warning: Missing mapping for {coin} or {ticker}. Skipping...")
    return g


def save_graph(graph, filename="graph.png"):
    
# Saving the graph as a PNG image


    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the full path for the image file
    file_path = os.path.join(script_dir, filename)

    # Generate positions for the nodes in a circular layout
    pos = nx.circular_layout(graph)  

    # Draw the graph
    plt.figure(figsize=(16, 16))  
    nx.draw_networkx(graph, pos, with_labels=True, node_size=3000, node_color="lightblue", font_size=15, font_weight="bold")

    # Add edge labels (weights)
    labels = nx.get_edge_attributes(graph, 'weight')  
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels, font_size=8)

    # Save the graph as a PNG image
    plt.savefig(file_path, format="png")
    plt.close()  
    print(f"Graph successfully saved as an image at {file_path}")


def calculate_path_weight(graph, path):
  
    # Calculate the total weight of a path in the graph.

    weight = 1.0
    for i in range(len(path) - 1):
        weight *= graph[path[i]][path[i + 1]]['weight']
    return weight

def detect_arbitrage(graph):

# Detect arbitrage opportunities in the graph and return detailed results.

    arbitrage_opportunities = []

    # Iterate through all pairs of nodes
    for node1, node2 in itertools.permutations(graph.nodes, 2):
        print(f"\npaths from {node1} to {node2} ----------------------------------")
        
        paths_to = list(nx.all_simple_paths(graph, node1, node2))
        paths_back = list(nx.all_simple_paths(graph, node2, node1))

        for path_to in paths_to:
            weight_to = calculate_path_weight(graph, path_to)
            for path_back in paths_back:
                weight_back = calculate_path_weight(graph, path_back)
                factor = weight_to * weight_back

                # Print paths with weights
                print(f"{path_to} {weight_to}")
                print(f"{path_back} {weight_back}")
                print(f"{factor}\n")

                # Store arbitrage details
                arbitrage_opportunities.append((path_to, path_back, factor))
    return arbitrage_opportunities

def output_results(opportunities):

# Print the arbitrage opportunities and the smallest and greatest path weight factors.

    if not opportunities:
        print("No arbitrage opportunities detected.")
        return

    # Find smallest and greatest factors
    smallest_factor = min(opportunities, key=lambda x: x[2])
    largest_factor = max(opportunities, key=lambda x: x[2])

    print("\nSmallest Paths weight factor:")
    print(f"Paths: {smallest_factor[0]}, {smallest_factor[1]}, Factor: {smallest_factor[2]:.8f}")

    print("\nGreatest Paths weight factor:")
    print(f"Paths: {largest_factor[0]}, {largest_factor[1]}, Factor: {largest_factor[2]:.8f}")


def main():

# Main function to execute the program.
  
    # Fetch exchange rates
    exchange_data = get_exchange_rates()
    if not exchange_data:
        print("Failed to fetch exchange rates. Exiting.")
        return
    
    # Build the graph
    graph = build_graph(exchange_data)
    print("Graph built successfully.")
    print("Nodes:", graph.nodes)
    print("Edges:", graph.edges(data=True))

    # save the graph 
    save_graph(graph, filename="crypto_exchange_graph.png")
    
    # Detect arbitrage opportunities
    arbitrage_opportunities = detect_arbitrage(graph)
    
    # Output results
    output_results(arbitrage_opportunities)

if __name__ == "__main__":
    main()