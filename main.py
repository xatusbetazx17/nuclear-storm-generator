from simulation.storm_simulator import simulate_storm
from control.ethical_protocol import check_ethics
from control.safety_mechanism import activate_safety
from energy.energy_converter import convert_energy

def main():
    print("⚡ Starting Nuclear Storm Generator Simulation...")

    energy_output = convert_energy(raw_nuclear_input=5000)  # in Megawatts
    if not check_ethics(energy_output):
        activate_safety()
        return

    simulate_storm(energy_output)

if __name__ == "__main__":
    main()
