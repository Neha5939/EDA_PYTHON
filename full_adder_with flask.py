from flask import Flask, render_template, send_file
from myhdl import *
import os

app = Flask(__name__)

# VCD File Location
VCD_FILE = "bench.vcd"

def full_adder(a, b, c, s, car):
    """Full Adder using MyHDL"""
    @always_comb
    def logic():
        s.next = (a and (not b) and (not c)) or ((not a) and b and (not c)) or ((not a) and (not b) and c) or (a and b and c)
        car.next = (b and c) or (a and c) or (a and b)
    return logic

def generate_vcd():
    """Runs simulation for all 8 input cases and generates a VCD file"""
    a, b, c, s, car = [Signal(bool(0)) for _ in range(5)]

    def bench():
        fadder_inst = full_adder(a, b, c, s, car)

        @instance
        def stimulus():
            for i in range(2):
                for j in range(2):
                    for k in range(2):
                        a.next, b.next, c.next = i, j, k
                        yield delay(10)  # Delay for signal processing
                        print(f"A={i}, B={j}, C={k} -> Sum={int(s)}, Carry={int(car)}")

        return fadder_inst, stimulus

    tb = traceSignals(bench)
    sim = Simulation(tb)
    sim.run()
    print(f"✅ VCD file generated: {VCD_FILE}")

@app.route("/")
def index():
    """Home page to show the results of all 8 input combinations"""
    generate_vcd()

    # Generate all 8 possible input combinations and compute expected outputs
    results = []
    for a in range(2):
        for b in range(2):
            for c in range(2):
                expected_sum = a ^ b ^ c
                expected_carry = (a & b) | (b & c) | (a & c)
                results.append({"a": a, "b": b, "c": c, "sum": expected_sum, "carry": expected_carry})

    vcd_available = os.path.exists(VCD_FILE)

    return render_template("index.html", results=results, vcd_available=vcd_available)

@app.route("/download_vcd")
def download_vcd():
    """Provide VCD file for download"""
    if os.path.exists(VCD_FILE):
        return send_file(VCD_FILE, as_attachment=True)
    else:
        return "VCD file not found!", 404

if __name__ == "__main__":
    app.run(debug=True)
