from flask import Flask, g
from myhdl import *
import sqlite3

app = Flask(__name__)
DATABASE = 'results.db'


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


def init_db():
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS half_adder_results (
                          id INTEGER PRIMARY KEY AUTOINCREMENT,
                          a INTEGER,
                          b INTEGER,
                          sum INTEGER,
                          carry INTEGER)''')
        db.commit()


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


def half_adder_gate(a, b, s, c):
    """
    Half Adder: Computes sum and carry.
    a, b -> Inputs
    s -> Sum
    c -> Carry
    """

    @always_comb
    def logic():
        s.next = a ^ b
        c.next = a and b

    return logic


# Simulation
@app.route('/simulate_half_adder_gate')
def simulate_half_adder_gate():
    db = get_db()
    cursor = db.cursor()

    a, b, s, c = [Signal(bool(0)) for _ in range(4)]
    truth_table = "<h3>Half Adder Truth Table</h3><pre>a b | s | c<br>------------<br>"

    def bench():
        and_inst = half_adder_gate(a, b, s, c)

        @instance
        def stimulus():
            nonlocal truth_table
            for i in range(2):
                for j in range(2):
                    a.next, b.next = i, j
                    yield delay(10)
                    cursor.execute("INSERT INTO half_adder_results (a, b, sum, carry) VALUES (?, ?, ?, ?)",
                                   (int(a), int(b), int(s), int(c)))
                    db.commit()
                    truth_table += f"{int(a)} {int(b)} | {int(s)} | {int(c)}<br>"
            return

        return and_inst, stimulus

    # Generate VCD File for waveform analysis
    tb = traceSignals(bench)
    sim = Simulation(tb)
    sim.run()
    print("VCD file generated as 'half_adder_gate.vcd'.")

    return truth_table + "</pre>"


if __name__ == '__main__':
    init_db()
    app.run(debug=True)