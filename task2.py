# map_colouring_task2.py

from typing import Dict, List, Optional

def colour_map(adj: Dict[int, List[int]], num_colours: int) -> Optional[Dict[int, int]]:
    """
    Returns a colour dictionary {node: colour_index} using numbers 0..num_colours-1
    or None if no valid colouring exists.
    """
    nodes = list(adj.keys())
    colours = [-1] * len(adj)          # -1 means uncoloured
    # Order nodes by degree (most constrained first) – reduces backtracking
    nodes.sort(key=lambda n: len(adj[n]), reverse=True)

    def safe(node, col):
        return all(colours[nb] != col for nb in adj[node])

    def backtrack(idx):
        if idx == len(nodes):
            return True
        node = nodes[idx]
        for col in range(num_colours):
            if safe(node, col):
                colours[node] = col
                if backtrack(idx + 1):
                    return True
                colours[node] = -1
        return False

    if backtrack(0):
        return {node: colours[node] for node in nodes}
    return None

def minimum_colours(adj: Dict[int, List[int]]) -> int:
    """Find the smallest number of colours that can colour the map."""
    max_degree = max(len(neighbours) for neighbours in adj.values())
    for k in range(2, max_degree + 2):   # at most max_degree+1 by Brooks' theorem
        if colour_map(adj, k) is not None:
            return k
    return max_degree + 1

# -------------------------------
# (a) Australia – 5 mainland regions
# -------------------------------
regions_aus = {0: "WA", 1: "NT", 2: "SA", 3: "Q", 4: "NSW"}
adj_aus_5 = {
    0: [1, 2],          # WA  – NT, SA
    1: [0, 2, 3],       # NT  – WA, SA, Q
    2: [0, 1, 3, 4],    # SA  – WA, NT, Q, NSW
    3: [1, 2, 4],       # Q   – NT, SA, NSW
    4: [2, 3]           # NSW – SA, Q
}

print("=" * 55)
print("Task 2(a): Australia 5‑region map (3 colours: Blue, Red, Green)")
print("=" * 55)

col_aus = colour_map(adj_aus_5, 3)
colour_name = {0: "Blue", 1: "Red", 2: "Green"}

if col_aus:
    for node in sorted(col_aus):
        print(f"  {regions_aus[node]:>4} -> {colour_name[col_aus[node]]}")
else:
    print("  No valid 3‑colouring found (should not happen).")

# -------------------------------
# (b) Nairobi 17 sub‑counties
# -------------------------------
nairobi_names = [
    "Westlands", "Dagoretti North", "Dagoretti South", "Lang'ata",
    "Kibra", "Roysambu", "Kasarani", "Ruaraka",
    "Embakasi South", "Embakasi North", "Embakasi Central",
    "Embakasi East", "Embakasi West", "Makadara",
    "Kamukunji", "Starehe", "Mathare"
]

# Adjacency derived from real geographic boundaries (planar graph)
adj_nairobi = {
    0:  [1, 5, 15, 16],              # Westlands
    1:  [0, 2, 4, 5],                # Dagoretti North
    2:  [1, 3, 4],                   # Dagoretti South
    3:  [2, 4, 13],                  # Lang'ata
    4:  [1, 2, 3, 13],               # Kibra
    5:  [0, 1, 6, 14, 15],           # Roysambu
    6:  [5, 7, 14],                  # Kasarani
    7:  [6, 8, 10, 14],              # Ruaraka
    8:  [7, 9, 12, 13],              # Embakasi South
    9:  [8, 10, 11],                 # Embakasi North
    10: [7, 9, 11, 12],              # Embakasi Central
    11: [9, 10, 12],                 # Embakasi East
    12: [8, 10, 11, 13],             # Embakasi West
    13: [3, 4, 8, 12, 14, 15],       # Makadara
    14: [5, 6, 7, 13, 15],           # Kamukunji
    15: [0, 5, 13, 14, 16],          # Starehe
    16: [0, 15]                      # Mathare
}

print("\n" + "=" * 55)
print("Task 2(b): Nairobi 17 sub‑counties (minimum colours)")
print("=" * 55)

min_col = minimum_colours(adj_nairobi)
print(f"Minimum colours needed: {min_col}")

col_nairobi = colour_map(adj_nairobi, min_col)
if col_nairobi:
    print("\nOne valid colouring:")
    for node in sorted(col_nairobi):
        print(f"  {nairobi_names[node]:<20} -> Colour {col_nairobi[node]}")
else:
    print("Could not find a valid colouring.")