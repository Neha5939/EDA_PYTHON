import matplotlib.pyplot as plt
import numpy as np

def half_adder_sum(a, b):
    return a ^ b  # XOR operation

def half_adder_carry(a, b):
    return a & b  # AND operation

# Define input combinations with extended time duration
inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
sum_output = [half_adder_sum(a, b) for a, b in inputs]
carry_output = [half_adder_carry(a, b) for a, b in inputs]

# Extend time duration for better visibility
time_steps = 5  # Number of steps per input
time = np.arange(len(inputs) * time_steps)

# Extend signal values for clear visibility
a_values = np.repeat([a for a, b in inputs], time_steps)
b_values = np.repeat([b for a, b in inputs], time_steps)
sum_values = np.repeat(sum_output, time_steps)
carry_values = np.repeat(carry_output, time_steps)

# Create figure with 4 subplots
fig, axs = plt.subplots(4, 1, figsize=(10, 6), sharex=True)

# Plot A
axs[0].step(time, a_values, where="post", linewidth=2, color="blue")
axs[0].set_ylabel("A")
axs[0].set_yticks([0, 1])
axs[0].grid(True, linestyle="--", alpha=0.7)

# Plot B
axs[1].step(time, b_values, where="post", linewidth=2, color="green")
axs[1].set_ylabel("B")
axs[1].set_yticks([0, 1])
axs[1].grid(True, linestyle="--", alpha=0.7)

# Plot Sum (A XOR B)
axs[2].step(time, sum_values, where="post", linewidth=2, color="red")
axs[2].set_ylabel("Sum (A XOR B)")
axs[2].set_yticks([0, 1])
axs[2].grid(True, linestyle="--", alpha=0.7)

# Plot Carry (A AND B)
axs[3].step(time, carry_values, where="post", linewidth=2, color="purple")
axs[3].set_ylabel("Carry (A AND B)")
axs[3].set_yticks([0, 1])
axs[3].set_xlabel("Time Steps")
axs[3].grid(True, linestyle="--", alpha=0.7)

# Set x-axis labels at transition points
plt.xticks(np.arange(0, len(time), time_steps), [f"{a},{b}" for a, b in inputs])

# Adjust layout
plt.suptitle("Half Adder Waveform (Enhanced Visibility)")
plt.tight_layout()
plt.show()
