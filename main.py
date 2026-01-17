import os

def load_input_data():
    blocks = []
    processes = []
    return blocks, processes

def run_first_fit(blocks, processes):
    print("Running First-Fit...")
    # implemented by Member 2
    pass

def run_best_fit(blocks, processes):
    print("Running Best-Fit...")
    # implemented by Member 3
    pass

def run_worst_fit(blocks, processes):
    print("Running Worst-Fit...")
    # implemented by Member 3
    pass

def show_menu():
    print("\n=== Memory Management Simulation ===")
    print("1. First-Fit")
    print("2. Best-Fit")
    print("3. Worst-Fit")
    print("0. Exit")

def main():
    blocks, processes = load_input_data()

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            run_first_fit(blocks, processes)
        elif choice == "2":
            run_best_fit(blocks, processes)
        elif choice == "3":
            run_worst_fit(blocks, processes)
        elif choice == "0":
            print("Exit program.")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
