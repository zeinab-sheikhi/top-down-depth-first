class TopDownDepthFirstNaiveRecognizer:
    
    def __init__(self, grammar):
        self.grammar = grammar

    def recognize(self, input_str):
        self.input = input_str
        self.index = 0  # pointer 

        # Start recognition from the top-level non-terminal
        if self.examine_non_terminal_symbol(self.grammar.axiom):
            return "recognized"
        else:
            return "not recognized"

    def examine_non_terminal_symbol(self, non_terminal_symbol):
        
        if self.index == len(self.input):
            # If we have consumed the entire input, recognition is successful
            return True

        for rule in self.grammar.rules:
            if rule.lhs == non_terminal_symbol:
                if self.examine_production_rule(rule):
                    return True
        return False

    def examine_production_rule(self, rule):
        original_index = self.index
        righ_side = rule.rhs
        for symbol in righ_side:
            if self.grammar.is_terminal(symbol):
                if not self.match_terminal(symbol):
                    # If the terminal symbol doesn't match, backtrack
                    
                    # self.reset_index(original_index)
                    self.index = original_index
                    
                    return False
            else:
                # Non-terminal symbol, recursively recognize it
                if not self.examine_non_terminal_symbol(symbol):
                    # If recognition fails, backtrack
                    self.index = original_index 
                    # self.reset_index(original_index)
                    
                    return False
        
        # Successfully recognized the entire production
        return True

    def match_terminal(self, terminal):
        
        if self.index < len(self.input) and self.input[self.index] == terminal.name:
            self.index += 1
            
            return True
        return False

    def reset_index(self, original_index):
        self.index = original_index
