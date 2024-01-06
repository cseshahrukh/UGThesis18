import re
import matplotlib.pyplot as plt

# Function to parse accuracy from a file
def parse_accuracy_from_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    rounds = re.findall(r'round\s+(\d+).*?test\s+accuracy\s+([\d.]+)', content, re.DOTALL)
    round_numbers, test_accuracies = zip(*map(lambda x: (int(x[0]), float(x[1])), rounds))
    return round_numbers, test_accuracies

# File paths and labels
file_paths = ['result_20clients_main2.txt', 'result_20clients_main3.txt', 'result_20clients_main4.txt', 'result_20clients_main6.txt']
labels = ['Main2_20client', 'Main3_20client', 'Main4_20client', 'Main6_20client']

# Plotting
plt.figure(figsize=(10, 6))

# Plot for the first file
with open(file_paths[0], 'r') as file:
    content = file.read()
rounds = re.findall(r'round\s+(\d+).*?test\s+accuracy\s+([\d.]+)', content, re.DOTALL)
round_numbers, test_accuracies = zip(*map(lambda x: (int(x[0]), float(x[1])), rounds))
plt.plot(round_numbers, test_accuracies, marker='o', linestyle='-', label=labels[0])

# Plot for the second file
with open(file_paths[1], 'r') as file:
    content = file.read()
rounds = re.findall(r'round\s+(\d+).*?test\s+accuracy\s+([\d.]+)', content, re.DOTALL)
round_numbers, test_accuracies = zip(*map(lambda x: (int(x[0]), float(x[1])), rounds))
plt.plot(round_numbers, test_accuracies, marker='o', linestyle='-', label=labels[1])

# Plot for the second file
with open(file_paths[2], 'r') as file:
    content = file.read()
rounds = re.findall(r'round\s+(\d+).*?test\s+accuracy\s+([\d.]+)', content, re.DOTALL)
round_numbers, test_accuracies = zip(*map(lambda x: (int(x[0]), float(x[1])), rounds))
plt.plot(round_numbers, test_accuracies, marker='o', linestyle='-', label=labels[2])


# Plot for the second file
with open(file_paths[3], 'r') as file:
    content = file.read()
rounds = re.findall(r'round\s+(\d+).*?test\s+accuracy\s+([\d.]+)', content, re.DOTALL)
round_numbers, test_accuracies = zip(*map(lambda x: (int(x[0]), float(x[1])), rounds))
plt.plot(round_numbers, test_accuracies, marker='o', linestyle='-', label=labels[3])


# Plot settings
plt.title('Accuracy vs Round Number')
plt.xlabel('Round Number')
plt.ylabel('Test Accuracy on Max and delta')
plt.grid(True)
plt.legend()
plt.show()
