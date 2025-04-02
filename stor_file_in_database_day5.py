from flask import Flask
from myhdl import *
import sqlite3

app = Flask(__name__)

# SQLite Database setup
def get_db():
    conn = sqlite3.connect('simulation_results.db')
    return conn

def create_table():
    # Create table if it doesn't exist
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vcd_files (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            truth_table TEXT,
            vcd_file TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_simulation_results(truth_table, vcd_file_path):
    # Insert simulation result into the database
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO vcd_files (truth_table, vcd_file)
        VALUES (?, ?)
    ''', (truth_table, vcd_file_path))
    conn.commit()
    conn.close()

# AND Gate Simulation
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

    vcd_file_path = "bench.vcd"  # Specify the path of the generated VCD file
    # After generating the VCD, store the truth table and VCD file path into the database
    insert_simulation_results(truth_table, vcd_file_path)

    return f"<h2>AND Gate Simulation</h2>{truth_table}<br>VCD file generated as '{vcd_file_path}'.<br>AND gate simulation completed."

# Flask route
@app.route('/')
def admin():
    return simulate_and_gate()  # Returns the truth table and stores results in the DB

# Run Flask app
if __name__ == '__main__':
    create_table()  # Create table if not exists
    app.run(debug=True)
