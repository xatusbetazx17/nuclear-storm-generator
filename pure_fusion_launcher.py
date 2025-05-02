from fusion_core import simulate_perfect_fusion, available_fuels
from plasma_stabilizer import stabilize_plasma, calculate_field_strength
from quantum_energy_grid import distribute_quantum_energy, estimate_conversion_efficiency

def main():
    print("🌡️ Starting Pure Thermonuclear Fusion Core Simulation...")

    # Show available fuels
    print("\n⚛️ Available Fuels:")
    for fuel in available_fuels():
        print(f" - {fuel}")

    # You can later make this dynamic (input()), but for now:
    selected_fuel = "Deuterium-Tritium"
    fuel_mass = 1.0  # kg

    # Simulate energy output
    fusion_output = simulate_perfect_fusion(selected_fuel, fuel_mass)
    print(f"\n⚛️ Fusion Output from {fuel_mass} kg of {selected_fuel}: {fusion_output:.2e} J")

    # Plasma confinement parameters
    field_strength = calculate_field_strength(fusion_output)
    stability = stabilize_plasma(fusion_output)
    print(f"\n🧲 Required Field Strength: {field_strength:.2e} T/m")
    print(f"🧠 Plasma Stability Achieved: {stability}")

    # Energy conversion and distribution
    conversion_efficiency = estimate_conversion_efficiency(fusion_output)
    print(f"\n⚡ Estimated Energy Conversion Efficiency: {conversion_efficiency * 100:.2f}%")

    # Quantum tech powered by fusion output
    apps = distribute_quantum_energy(fusion_output)
    print("\n🚀 Quantum Energy Applications Enabled:")
    for app in apps:
        print(f"  - {app}")

if __name__ == "__main__":
    main()

