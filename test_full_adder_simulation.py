from myhdl import *

def full_adder(a, b, c, s, car):
    @always_comb
    def logic():
        s.next = (a and (not b) and (not c)) or ((not a) and b and (not c)) or ((not a) and (not b) and c) or (a and b and c)
        car.next = (b and c) or (a and c) or (a and b)
    return logic

# Testbench
def test_full_adder():
    a, b, c, s, car = [Signal(bool(0)) for _ in range(5)]

    fadder_inst = full_adder(a, b, c, s, car)

    @instance
    def stimulus():
        print("a b c | s car")
        print("--------------")
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    a.next, b.next, c.next = i, j, k
                    yield delay(10)  # Allow signal propagation

                    # Expected outputs
                    expected_s = (i ^ j ^ k)  # Sum logic
                    expected_car = (i & j) | (j & k) | (i & k)  # Carry logic

                    # Print results
                    print(f'{int(a)} {int(b)} {int(c)} | {int(s)} {int(car)}')

                    # Assertions for verification
                    assert int(s) == expected_s, f"Test failed for {i}, {j}, {k}: Expected sum={expected_s}, Got {int(s)}"
                    assert int(car) == expected_car, f"Test failed for {i}, {j}, {k}: Expected carry={expected_car}, Got {int(car)}"

        print("All test cases passed!")

    return fadder_inst, stimulus

# Run test
tb = traceSignals(test_full_adder)
sim = Simulation(tb)
sim.run()
