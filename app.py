import streamlit as st

# Page Configuration
st.set_page_config(page_title="Mechanical Engineering Toolkit", layout="wide")

# Header Section with User Credentials
st.title("Mechanical Unit Converter & Density Checker")
st.sidebar.markdown(f"### Developed By:\n**Name:** muhammad rayyan\n**Roll No:** 25-ME-184")
st.write("---")

# Navigation
option = st.selectbox("Choose a Tool", ["Unit Converter", "Material Density Checker"])

# --- TOOL 1: Unit Converter ---
if option == "Unit Converter":
    st.header("⚙️ Mechanical Unit Converter")
    
    col1, col2 = st.columns(2)
    
    with col1:
        category = st.selectbox("Select Category", ["Pressure", "Power", "Force"])
        value = st.number_input("Enter Value", value=1.0)

    if category == "Pressure":
        # Conversion: 1 bar = 100,000 Pa = 14.5038 psi
        st.subheader("Pressure Conversions")
        units = {"Pascal (Pa)": 1, "Bar": 100000, "PSI": 6894.76}
        base_unit = st.selectbox("From Unit", list(units.keys()))
        
        value_in_pascal = value * units[base_unit]
        
        st.success(f"{value} {base_unit} is equal to:")
        for unit, factor in units.items():
            st.write(f"- **{value_in_pascal / factor:.4f}** {unit}")

    elif category == "Power":
        # Conversion: 1 HP = 745.7 Watts
        st.subheader("Power Conversions")
        units = {"Watts (W)": 1, "Kilowatts (kW)": 1000, "Horsepower (hp)": 745.7}
        base_unit = st.selectbox("From Unit", list(units.keys()))
        
        value_in_watts = value * units[base_unit]
        
        st.success(f"{value} {base_unit} is equal to:")
        for unit, factor in units.items():
            st.write(f"- **{value_in_watts / factor:.4f}** {unit}")

    elif category == "Force":
        # Conversion: 1 Newton = 0.2248 lbs
        st.subheader("Force Conversions")
        units = {"Newton (N)": 1, "Kilonewton (kN)": 1000, "Pound-force (lbf)": 4.448}
        base_unit = st.selectbox("From Unit", list(units.keys()))
        
        value_in_newtons = value * units[base_unit]
        
        st.success(f"{value} {base_unit} is equal to:")
        for unit, factor in units.items():
            st.write(f"- **{value_in_newtons / factor:.4f}** {unit}")

# --- TOOL 2: Material Density Checker ---
else:
    st.header("⚖️ Material Density Checker")
    st.info("Quickly find the density of common engineering materials.")
    
    # Dictionary of Materials (kg/m^3)
    densities = {
        "Steel": 7850,
        "Aluminum": 2700,
        "Copper": 8960,
        "Titanium": 4500,
        "Cast Iron": 7200,
        "Concrete": 2400,
        "Water": 1000,
        "Air": 1.225
    }
    
    material = st.selectbox("Select Material", list(densities.keys()))
    search_query = st.text_input("Or search for a material:")
    
    final_material = search_query.capitalize() if search_query else material
    
    if final_material in densities:
        density_val = densities[final_material]
        st.metric(label=f"Density of {final_material}", value=f"{density_val} kg/m³")
    else:
        st.error("Material not found in database.")

# Footer
st.write("---")
st.caption(f"© 2026 muhammad rayyan (25-ME-184) - Mechanical Engineering App")
