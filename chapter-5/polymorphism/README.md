Check if rectangles overlap

ASSIGNMENT
Let's write the overlaps() method, it should return True if the rectangles overlap, and False otherwise. Keep in mind that we want our overlap to be inclusive. If the rectangle's edges are on top of each other, that counts as overlapping.

The logic for two overlapping rectangles, A and B, involves 4 conditions. If all of the following conditions are True then the rectangles overlap:

A's left edge is left of B's right edge
A's right edge is right of B's left edge
A's top edge is above B's bottom edge
A's bottom edge is below B's top edge