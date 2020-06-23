"""
 * depthfirst.py
 *
 * Minor programming Universiteit van Amsterdam - Programmeertheorie - RailNL
 * Daphne Westerdijk, Willem Henkelman, Lieke Kollen
 *
 * Constructive algorithm that searches a tree data structure. 
 * It starts at the root node and first explores all the nodes in the first depth before continuing to next depth
"""

from .depthfirst import Depthfirst

class Breadthfirst(Depthfirst):
    """
    class that finds train routes taking into account the heuristics using a breadth first algorithm
    """

    def get_next_state(self, stack):
        """
        method that gets the next item from the stack
        """

        return stack.pop(0)