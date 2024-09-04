import streamlit as st

def calculate_total_cost_in_india(price_in_india, weight_in_kg, shipping_charge_per_kg):
    # Calculate shipping cost
    shipping_cost = weight_in_kg * shipping_charge_per_kg
    
    # Total cost is price in India plus shipping cost
    total_cost_in_india = price_in_india + shipping_cost
    return total_cost_in_india

def calculate_total_cost_in_usa(price_in_usa):
    # In the USA, the total cost is just the price in the USA
    total_cost_in_usa = price_in_usa
    return total_cost_in_usa

def main():
    st.title("Price Comparison: India vs USA")

    # Inputs
    st.header("Enter the item details:")
    price_in_india = st.number_input("Price in India (INR):", min_value=0.0, format="%.2f")
    weight_in_grams_india = st.number_input("Weight of the item in India (grams):", min_value=0.0, format="%.2f")
    shipping_charge_per_kg = st.number_input("Shipping charge per kg (INR):", min_value=0.0, format="%.2f")
    price_in_usa = st.number_input("Price in USA (USD):", min_value=0.0, format="%.2f")
    weight_in_grams_usa = st.number_input("Weight of the item in USA (grams):", min_value=0.0, format="%.2f")
    
    # Convert to USD (assuming INR to USD conversion rate)
    conversion_rate = st.number_input("INR to USD conversion rate:", min_value=0.0, value=82.0, format="%.2f")
    
    # Convert weights from grams to kilograms
    weight_in_kg_india = weight_in_grams_india / 1000
    weight_in_kg_usa = weight_in_grams_usa / 1000
    
    # Calculating total cost if bought in India and shipped to the USA
    if st.button("Calculate"):
        total_cost_in_india_inr = calculate_total_cost_in_india(price_in_india, weight_in_kg_india, shipping_charge_per_kg)
        total_cost_in_india_usd = total_cost_in_india_inr / conversion_rate
        
        total_cost_in_usa = calculate_total_cost_in_usa(price_in_usa) * conversion_rate
        
        # st.subheader("Total cost comparison:")
        # st.write(f"Total cost if bought in India and shipped to the USA: {total_cost_in_india_usd:.2f} USD")
        # st.write(f"Total cost if bought in the USA: {total_cost_in_usa:.2f} USD")
        
        # Per kg price comparison
        price_per_kg_in_india_usd = total_cost_in_india_inr / weight_in_kg_india if weight_in_kg_india > 0 else 0
        price_per_kg_in_usa = price_in_usa * conversion_rate/ weight_in_kg_usa if weight_in_kg_usa > 0 else 0

        st.subheader("Per kilogram price comparison:")
        st.write(f"Price per kg if bought in India and shipped to the USA: {price_per_kg_in_india_usd:.2f} INR/kg")
        st.write(f"Price per kg if bought in the USA: {price_per_kg_in_usa:.2f} INR/kg")
        
    
        # Determine which is cheaper per kg
        if price_per_kg_in_india_usd < price_per_kg_in_usa:
            st.success("The per kg price is cheaper if bought in India and shipped.")
        elif price_per_kg_in_india_usd > price_per_kg_in_usa:
            st.success("The per kg price is cheaper if bought in the USA.")
        else:
            st.info("The per kg price is the same in both cases.")

if __name__ == "__main__":
    main()
