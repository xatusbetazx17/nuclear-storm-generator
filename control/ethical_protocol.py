def check_ethics(energy_output):
    print("🧠 Checking ethical parameters...")
    if energy_output > 3000:
        print("⚠️ Ethical boundary exceeded. Storm generation is NOT allowed.")
        return False
    print("✅ Ethical check passed.")
    return True
