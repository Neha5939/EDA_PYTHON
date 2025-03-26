import time
import pytest
from Half_adder import half_adder_sum, half_adder_carry

# Define the log file
log_file = "test_execution_HA_log.txt"

# Ensure the file is created (overwrite on each run)
with open(log_file, "w") as f:
    f.write("Execution Log - Half Adder Tests\n")

@pytest.mark.parametrize("a, b, c", [(0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 0)])
def test_half_adder_sum(a, b, c):
    start_time = time.perf_counter()  # Start time
    result = half_adder_sum(a, b)
    end_time = time.perf_counter()  # End time
    execution_time = end_time - start_time

    log_message = f"half_adder_sum({a}, {b}) => Expected: {c}, Got: {result}, Time: {execution_time:.10f} sec"

    print(log_message)
    with open(log_file, "a") as f:
        f.write(log_message + "\n")

    assert result == c

@pytest.mark.parametrize("a, b, c", [(0, 0, 0), (0, 1, 0), (1, 0, 0), (1, 1, 1)])
def test_half_adder_carry(a, b, c):
    start_time = time.perf_counter()  # Start time
    result = half_adder_carry(a, b)
    end_time = time.perf_counter()  # End time
    execution_time = end_time - start_time

    log_message = f"half_adder_carry({a}, {b}) => Expected: {c}, Got: {result}, Time: {execution_time:.10f} sec"

    print(log_message)
    with open(log_file, "a") as f:
        f.write(log_message + "\n")

    assert result == c
