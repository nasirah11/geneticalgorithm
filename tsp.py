import streamlit as st
import matplotlib.pyplot as plt
from itertools import permutations
import random
import numpy as np
import seaborn as sns

# --- Page setup ---
st.title("Travelling Salesman Problem (TSP) using Genetic Algorithm")

# City data
x = [0,3,6,7,15,10,16,5,8,1.5]
y = [1,2,1,4.5,-1,2.5,11,6,9,12]
cities_names = ["Gliwice", "Cairo", "Rome", "Krakow", "Paris", "Alexandria", "Berlin", "Tokyo", "Rio", "Budapest"]
city_coords = dict(zip(cities_names, zip(x, y)))

# Parameters
n_population = 50
crossover_per = 0.8
mutation_per = 0.2
n_generations = 50
colors = sns.color_palette("pastel", len(cities_names))

# --- (Your GA functions stay the same here) ---
# ... include your dist_two_cities(), initial_population(), etc.

# --- Run GA ---
with st.spinner("Running Genetic Algorithm..."):
    best_mixed_offspring = run_ga(cities_names, n_population, n_generations, crossover_per, mutation_per)
    total_dist_all_individuals = [total_dist_individual(ind) for ind in best_mixed_offspring]
    index_minimum = np.argmin(total_dist_all_individuals)
    minimum_distance = min(total_dist_all_individuals)
    shortest_path = best_mixed_offspring[index_minimum]

# --- Plot the best route ---
x_shortest = [city_coords[c][0] for c in shortest_path] + [city_coords[shortest_path[0]][0]]
y_shortest = [city_coords[c][1] for c in shortest_path] + [city_coords[shortest_path[0]][1]]

fig, ax = plt.subplots(figsize=(12, 8))
ax.plot(x_shortest, y_shortest, '--go', linewidth=2.5)
for i, txt in enumerate(shortest_path):
    ax.annotate(f"{i+1}- {txt}", (x_shortest[i], y_shortest[i]), fontsize=12)

plt.title(f"TSP Best Route using GA\nTotal Distance: {round(minimum_distance, 3)}")
st.pyplot(fig)
