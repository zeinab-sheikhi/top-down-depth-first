from grammar import Grammar, Symbol, Rule
from top_down_depth_first import TopDownDepthFirstNaiveRecognizer

sym_S = Symbol("S")
sym_NP = Symbol("NP")
sym_VP = Symbol("VP")
sym_DET = Symbol("DET")
sym_N = Symbol("N")
sym_PN = Symbol("PN")
sym_V = Symbol("V")
sym_the = Symbol("the")
sym_a = Symbol("a")
sym_truck = Symbol("truck")
sym_experiment = Symbol("experiment")
sym_Sabine = Symbol("Sabine")
sym_Fred = Symbol("Fred")
sym_Jamy = Symbol("Jamy")
sym_sees = Symbol("sees")
sym_prepares = Symbol("prepares")

g1 = Grammar(
    # symbols
    [sym_S, sym_NP, sym_VP, sym_DET, sym_N, sym_PN, sym_V, sym_the, sym_a, sym_truck, sym_experiment, sym_Sabine, sym_Fred, sym_Jamy, sym_sees, sym_prepares],
    
    # axiom
    sym_S,
    
    [
        Rule(sym_S, [sym_NP, sym_VP]),
        Rule(sym_NP, [sym_DET, sym_N]),
        Rule(sym_NP, [sym_PN]),
        Rule(sym_VP, [sym_V]),
        Rule(sym_VP, [sym_V, sym_NP]),
        Rule(sym_DET, [sym_the]),
        Rule(sym_DET, [sym_a]),
        Rule(sym_N, [sym_truck]),
        Rule(sym_N, [sym_experiment]),
        Rule(sym_PN, [sym_Sabine]),
        Rule(sym_PN, [sym_Fred]),
        Rule(sym_PN, [sym_Jamy]),
        Rule(sym_V, [sym_sees]),
        Rule(sym_V, [sym_prepares]),
    ],

    "g1"
)

sym_S = Symbol("S")
sym_NP = Symbol("NP")
sym_VP = Symbol("VP")
sym_Aux = Symbol('AUX')
sym_DET = Symbol("DET")
sym_Noun = Symbol('Noun')
sym_V = Symbol("V")
sym_book = Symbol('book')
sym_that = Symbol('that')
sym_flight = Symbol('flight')
sym_does = Symbol('does')


g2 = Grammar(
    [sym_S, sym_NP, sym_VP, sym_V, sym_book, sym_that, sym_flight, sym_Noun, sym_does, sym_DET, sym_Aux], 
    sym_S, 
    [
        Rule(sym_S, [sym_NP, sym_VP]),
        Rule(sym_S, [sym_Aux, sym_NP, sym_VP]),
        Rule(sym_S, [sym_VP]),
        Rule(sym_NP, [sym_DET, sym_Noun]),
        Rule(sym_VP, [sym_V]),
        Rule(sym_VP, [sym_V, sym_NP]),
        Rule(sym_V, [sym_book]),
        Rule(sym_DET, [sym_that]),
        Rule(sym_Aux, [sym_does]),
        Rule(sym_Noun, [sym_flight]),
    ],
    "g2"
)

sym_A = Symbol("A")
sym_b = Symbol("b")
sym_epsilon = Symbol("")

g3 = Grammar(
    [sym_S, sym_A, sym_a, sym_b],
    sym_S,
    [
        Rule(sym_S, [sym_A, sym_epsilon]),
        Rule(sym_A, [sym_A, sym_a]),
    ],
    "g3",
)

# --------------
print("\n")
words = [["Sabine", "sees", "a", "truck"], ["Sabine", "sees", "Fred"], ["Fred", "prepares", "Jamy"]]

recognizer1 = TopDownDepthFirstNaiveRecognizer(grammar=g1)
for word in words:
    print(f"{' '.join(word)}")
    print(recognizer1.recognize(word), "\n")

word4 = ["book", "that", "flight"]
recognizer2 = TopDownDepthFirstNaiveRecognizer(grammar=g1)
print(" ".join(word4))
print(recognizer2.recognize(input_str=word4))

# word6 = ["a", "a", "a", "a", "a"]
# recognizer3 = TopDownDepthFirstNaiveRecognizer(grammar=g3)
# recognizer3.recognize(input_str=word6)
