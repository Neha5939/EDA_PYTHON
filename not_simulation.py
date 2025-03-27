from myhdl import *


# NOT Gate definition
def Not_Gate(a, c):
    @always_comb
    def logic():
        c.next = not a

    return logic


# Simulation function
def simulate_not_gate():
    a, c = [Signal(bool(0)) for _ in range(2)]  # Fix: Only 2 signals needed

    def bench():
        not_inst = Not_Gate(a, c)  # Instantiate NOT Gate

        @instance
        def stimulus():
            print("a | c")
            print("-------")
            for i in range(2):  # Loop through 0 and 1
                a.next = bool(i)  # Update input signal
                yield delay(10)  # Wait for signal propagation
                print(f'{int(a)} | {int(c)}')  # Print output

        return not_inst, stimulus

    # Generate VCD waveform file
    tb = traceSignals(bench)  # Fix: traceSignals applied to bench()
    sim = Simulation(tb)
    sim.run()
    print("VCD file generated as 'not_gate.vcd'.")


# Run the NOT gate simulation
def test():
    simulate_not_gate()


test()
