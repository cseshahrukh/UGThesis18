import re
import matplotlib.pyplot as plt

def parse_accuracy_from_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Use regular expression to find round numbers and corresponding test accuracies
    rounds = re.findall(r'round\s+(\d+).*?test\s+accuracy\s+([\d.]+)', content, re.DOTALL)

    round_numbers, test_accuracies = zip(*map(lambda x: (int(x[0]), float(x[1])), rounds))
    return round_numbers, test_accuracies

def plot_accuracy_vs_round(file_path):
    round_numbers, test_accuracies = parse_accuracy_from_file(file_path)

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(round_numbers, test_accuracies, marker='o', linestyle='-', color='b')
    plt.title('Accuracy vs Round Number')
    plt.xlabel('Round Number')
    plt.ylabel('Test Accuracy on Max and delta')
    plt.grid(True)
    plt.show()

# Replace 'your_file.txt' with the actual path to your text file
plot_accuracy_vs_round('result_main4.txt')
