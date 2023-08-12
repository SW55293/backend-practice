Check if rectangles overlap

ASSIGNMENT
Let's write the overlaps() method, it should return True if the rectangles overlap, and False otherwise. Keep in mind that we want our overlap to be inclusive. If the rectangle's edges are on top of each other, that counts as overlapping.

The logic for two overlapping rectangles, A and B, involves 4 conditions. If all of the following conditions are True then the rectangles overlap:

A's left edge is left of B's right edge
A's right edge is right of B's left edge
A's top edge is above B's bottom edge
A's bottom edge is below B's top edge

### ----
ASSIGNMENT
First, complete the Dragon's constructor. The dragon needs one more private data member: __hit_box. The hitbox is a Rectangle object. You've been provided with the height, width, and center position (pos_x, pos_y) of the dragon.

`
center = pos_x = 2, pos_y = 1
Height = 2
Width = 4
`

IN_AREA() METHOD()
Next, you'll need to override the in_area method. Create a new rectangle object with the given corner positions, and use the rectangle's overlaps method to check if the Dragon is inside it. This method should return a boolean value.