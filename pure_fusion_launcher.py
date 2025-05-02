from fusion_core import simulate_perfect_fusion
from plasma_stabilizer import stabilize_plasma
from quantum_energy_grid import distribute_quantum_energy

def main():
    print("🌡️ Starting Pure Thermonuclear Fusion Core Simulation...")

    fusion_output = simulate_perfect_fusion("Deuterium-Tritium", 1.0)  # 1 kg input
    print(f"⚛️ Fusion Output: {fusion_output:.2e} J")

    stability = stabilize_plasma(fusion_output)
    print(f"🧠 Plasma Stability Achieved: {stability}")

    apps = distribute_quantum_energy(fusion_output)
    print("\n🚀 Quantum Energy Applications Enabled:")
    for app in apps:
        print(f"  - {app}")

if __name__ == "__main__":
    main()
