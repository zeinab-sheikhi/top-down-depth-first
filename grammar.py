class Grammar:
    
    def __init__(self, symbols, axiom, rules, name):
        
        self.symbols = symbols              # list of Symbol
        self.axiom = axiom                  # Symbol
        self.rules = rules                  # list of Rule
        self.name = name                    # string
        self.non_terminals = set()           # set of Symbol
        self.terminals = set()              # set of Symbol
        
        for rule in rules:
            self.non_terminals.add(rule.lhs)
        
        self.terminals = set(symbols) - self.non_terminals
        
    def is_non_terminal(self, symbol):
        return symbol in self.non_terminals
    
    def is_terminal(self, symbol):
        return symbol in self.terminals


class Symbol:
    
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Rule:
    
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs

    def __str__(self):
        return str(self.lhs) + " --> [" + ",".join([str(s) for s in self.rhs]) + "]"
