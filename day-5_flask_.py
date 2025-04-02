from flask import Flask
from myhdl import *

app = Flask(__name__)

def AND_Gate(a, b, c):
    @always_comb
    def logic():
        c.next = a & b
    return logic

# Simulation function
def simulate_and_gate():
    a, b, c = [Signal(bool(0)) for _ in range(3)]
    truth_table = "a b | c<br>-------<br>"

    def bench():
        and_inst = AND_Gate(a, b, c)

        @instance
        def stimulus():
            nonlocal truth_table
            for i in range(2):
                for j in range(2):
                    a.next, b.next = i, j
                    yield delay(10)
                    truth_table += f"{int(a)} {int(b)} | {int(c)}<br>"
            return

        return and_inst, stimulus

    # Generate VCD
    tb = traceSignals(bench)
    sim = Simulation(tb)
    sim.run()

    return f"<h2>AND Gate Simulation</h2>{truth_table}<br>VCD file generated as 'and_gate.vcd'.<br>AND gate simulation completed."

# Flask route
@app.route('/')
def admin():
    return simulate_and_gate()  # Returns the truth table

# Run Flask app
if __name__ == '__main__':
    app.run(debug=True)
