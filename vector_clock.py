# vector_clock.py
# ----------------
# Implements a simple Vector Clock system with increment, update, and compare functions.

class VectorClock:
    def __init__(self, node_id):
        """
        Initialize a vector clock for this node.
        Example: node_id = 'A'
        """
        self.clock = {}
        self.node_id = node_id
        self.clock[node_id] = 0

    def increment(self):
        """Increment local node’s counter (for a local event)."""
        self.clock[self.node_id] += 1

    def update(self, other_clock):
        """
        Merge with another vector clock.
        Takes the maximum count for each node.
        """
        for node, time in other_clock.items():
            if node in self.clock:
                self.clock[node] = max(self.clock[node], time)
            else:
                self.clock[node] = time

    def compare(self, other_clock):
        """
        Compare this vector clock with another.
        Returns one of:
        - 'happens-before'  if self < other
        - 'happens-after'   if self > other
        - 'equal'           if both identical
        - 'concurrent'      if neither dominates
        """
        less = greater = False

        all_nodes = set(self.clock.keys()).union(set(other_clock.keys()))

        for node in all_nodes:
            self_val = self.clock.get(node, 0)
            other_val = other_clock.get(node, 0)

            if self_val < other_val:
                less = True
            elif self_val > other_val:
                greater = True

        if less and not greater:
            return "happens-before"
        elif greater and not less:
            return "happens-after"
        elif not less and not greater:
            return "equal"
        else:
            return "concurrent"

    def get_clock(self):
        """Return the dictionary form of the vector clock."""
        return self.clock
