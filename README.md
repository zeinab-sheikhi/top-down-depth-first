# Top Down Depth First Naive Parser
This repository contains Python implementations of the Top Down Depth First Naive Parser parsing algorithm.

In top-down parsing we start at the most abstract level (the level of sentences) and work down to the most concrete level (the level of words). So, given an input string, we start out by assuming that it is a sentence, and then try to prove that it really is one by using the rules left-to-right. 

Depth first search means that whenever there is more than one rule that could be applied at one point, we explore one possibility and only look at the others when this one fails.

