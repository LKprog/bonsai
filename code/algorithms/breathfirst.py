"""
 * depthfirst.py
 *
 * Minor programming Universiteit van Amsterdam - Programmeertheorie - RailNL
 * Daphne Westerdijk, Willem Henkelman, Lieke Kollen
"""

from .depthfirst import Depthfirst

class Breadthfirst(Depthfirst):
    """
    class that finds train routes taking into account the heuristics using a breath first algorithm.
    """

    def get_next_state(self, stack):
    """
    method that gets the next item from the stack.
    """
    return stack.pop(0)