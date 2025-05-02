def simulate_perfect_fusion(fuel_type, mass_kg):
    """Simulates 100% efficient fusion burn based on fuel type."""
    energy_density = {
        "Deuterium-Tritium": 3.4e14,  # J/kg
        "Helium-3": 5.8e14            # J/kg
    }
    if fuel_type not in energy_density:
        raise ValueError("Unsupported fusion fuel.")

    print(f"⚛️ Simulating {fuel_type} fusion at 100% efficiency...")
    return mass_kg * energy_density[fuel_type]
