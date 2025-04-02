from myhdl import *
def full_adder(a,b,c,s,car):
    @always_comb
    def logic():
        s.next= (a and (not b) and (not c)) or ((not a) and b and (not c)) or ((not a) and (not b) and c) or (a and b and c)
        car.next= (b and c) or (a and c) or (a and b)
    return logic

#simulation
def simulate_full_adder():
    a,b,c,s,car=[Signal(bool(0)) for _ in range(5)]
    def bench():
        fadder_inst=full_adder(a,b,c,s,car)
        @instance
        def stimulus():
            print("a b | c")
            print("-------")
            for i in range(2):
                for j in range(2):
                    for k in range(2):
                        a.next, b.next, c.next=i,j,k
                        yield delay(10)
                        print(f'{int(a)} {int(b)} | {int(c)} | {int(s)} | {int(car)}')
        return fadder_inst,stimulus
    #generate vcd
    tb=traceSignals(bench)
    sim=Simulation(tb)
    sim.run()
    print("VCD file generated as bench.vcd")
#run
def test():
    simulate_full_adder()
test()