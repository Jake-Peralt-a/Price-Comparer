import streamlit as st

def convert_weight_to_kg(weight, unit):
    # Conversion factors to kilograms
    if unit == "Grams":
        return weight / 1000
    elif unit == "Kilograms":
        return weight
    elif unit == "Ounces":
        return weight * 0.0283495
    elif unit == "Pounds":
        return weight * 0.453592
    else:
        return 0

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
    
    # Price in India
    price_in_india = st.text_input("Price in India (INR):")
    price_in_india = float(price_in_india) if price_in_india else 0
    
    # Weight in India and unit selection
    weight_in_grams_india = st.text_input("Weight of the item in India:")
    weight_in_grams_india = float(weight_in_grams_india) if weight_in_grams_india else 0
    
    unit_in_india = st.selectbox("Select unit of weight for the item in India:", ["Grams", "Kilograms", "Ounces", "Pounds"], index=0)
    
    # Shipping charge
    shipping_charge_per_kg = st.text_input("Shipping charge per kg (INR):",value=660)
    shipping_charge_per_kg = float(shipping_charge_per_kg) if shipping_charge_per_kg else 660
    
    # Price in USA
    price_in_usa = st.text_input("Price in USA (USD):")
    price_in_usa = float(price_in_usa) if price_in_usa else 0
    
    # Weight in USA and unit selection
    weight_in_grams_usa = st.text_input("Weight of the item in USA:")
    weight_in_grams_usa = float(weight_in_grams_usa) if weight_in_grams_usa else 0
    
    unit_in_usa = st.selectbox("Select unit of weight for the item in USA:", ["Grams", "Kilograms", "Ounces", "Pounds"], index=0)
    
    # Convert to USD (assuming INR to USD conversion rate)
    conversion_rate = st.text_input("INR to USD conversion rate:", value="83.5")
    conversion_rate = float(conversion_rate) if conversion_rate else 83.5
    
    # Convert weights to kilograms
    weight_in_kg_india = convert_weight_to_kg(weight_in_grams_india, unit_in_india)
    weight_in_kg_usa = convert_weight_to_kg(weight_in_grams_usa, unit_in_usa)
    
    # Calculating total cost if bought in India and shipped to the USA
    if st.button("Calculate"):
        total_cost_in_india_inr = calculate_total_cost_in_india(price_in_india, weight_in_kg_india, shipping_charge_per_kg)
        total_cost_in_india_usd = total_cost_in_india_inr / conversion_rate
        
        total_cost_in_usa = calculate_total_cost_in_usa(price_in_usa) * conversion_rate
        
        # Per kg price comparison
        price_per_kg_in_india_inr = total_cost_in_india_inr / weight_in_kg_india if weight_in_kg_india > 0 else 0
        price_per_kg_in_usa = price_in_usa * conversion_rate / weight_in_kg_usa if weight_in_kg_usa > 0 else 0

        st.subheader("Per kilogram price comparison:")
        st.write(f"Price per kg if bought in India and shipped to the USA: {price_per_kg_in_india_inr:.2f} INR/kg")
        st.write(f"Price per kg if bought in the USA: {price_per_kg_in_usa:.2f} INR/kg")
        
        # Determine which is cheaper per kg
        if price_per_kg_in_india_inr < price_per_kg_in_usa:
            st.success("The per kg price is cheaper if bought in India and shipped.")
        elif price_per_kg_in_india_inr > price_per_kg_in_usa:
            st.success("The per kg price is cheaper if bought in the USA.")
        else:
            st.info("The per kg price is the same in both cases.")

if __name__ == "__main__":
    main()
