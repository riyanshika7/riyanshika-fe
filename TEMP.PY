def read_temps_from_input():
    print("Enter temperatures separated by spaces (e.g. 30 32 29):")
    line = input("> ").strip()
    parts = line.split()
    temps = []
    for p in parts:
        try:
            temps.append(float(p))
        except ValueError:
            print(f"Warning: '{p}' skipped (not a number).")
    return temps

def analyze(temps):
    if not temps:
        print("No temperature data.")
        return
    avg = sum(temps) / len(temps)
    mn = min(temps)
    mx = max(temps)
    above = [t for t in temps if t > avg]
    print(f"Count: {len(temps)}  Min: {mn}  Max: {mx}  Average: {avg:.2f}")
    print("Above-average days:", above)

def main():
    temps = read_temps_from_input()
    analyze(temps)

main()
