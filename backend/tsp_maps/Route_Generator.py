import streamlit as st
from geopy.geocoders import Nominatim
import numpy as np
from scipy.spatial.distance import pdist, squareform
from tsp_solver.greedy import solve_tsp

st.title("Fastest Route Generator")

st.write("Enter addresses (one per line) in the format: streetname housenumber city")

addresses_input = st.text_area("Addresses", value="Neude 11 Utrecht\nMuseumstraat 1 Amsterdam\nPr. Irenepad 1 Den Haag", height=200)
addresses = [line.strip() for line in addresses_input.split('\n') if line.strip()]

max_index = max(len(addresses) - 1, 0)
start_idx = st.number_input("Start index (0-based)", min_value=0, max_value=max_index, value=0)
end_idx = st.number_input("End index (0-based)", min_value=0, max_value=max_index, value=max_index)

if st.button("Calculate Fastest Route"):
    if len(addresses) < 2:
        st.error("Please enter at least two addresses.")
    else:
        geolocator = Nominatim(user_agent="RouteGeneratorStreamlit")
        latlons = []
        failed = []
        for addr in addresses:
            try:
                location = geolocator.geocode(addr)
                if location:
                    latlons.append((location.latitude, location.longitude))
                else:
                    failed.append(addr)
            except Exception as e:
                failed.append(addr)
        if failed:
            st.warning(f"Could not geocode: {', '.join(failed)}")
        if len(latlons) < 2:
            st.error("Not enough valid addresses to calculate a route.")
        else:
            matrix = squareform(pdist(np.array(latlons)))
            matrix[:, start_idx] = 0  # Ensure start point is fixed
            path = solve_tsp(matrix, endpoints=(start_idx, end_idx))
            
            def format_address(addr):
                # Split by comma, strip, and join with '+'
                parts = [p.strip().replace(' ', '+') for p in addr.split(',')]
                return '+'.join(parts) + '/'
            
            url = 'https://www.google.nl/maps/dir/'
            for i in path:
                url += format_address(addresses[i])
            st.markdown(f"[Open Route in Google Maps]({url})")
            st.write("Order of addresses:")
            for idx in path:
                st.write(f"{addresses[idx]}")
