#!/usr/bin/python3
def canUnlockAll(boxes):
    """
    Determine if all the boxes can be opened.
    
    Args:
        boxes (list): A list of lists where each inner list represents keys inside a box.
        
    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)  # Number of boxes
    opened = [False] * n  # Track which boxes are opened
    opened[0] = True  # The first box is always open
    stack = [0]  # Start with box 0
    
    # Use DFS to visit all boxes we can open
    while stack:
        current_box = stack.pop()  # Take the current box to explore
        for key in boxes[current_box]:
            if key < n and not opened[key]:  # Valid key and box not opened yet
                opened[key] = True  # Mark the box as opened
                stack.append(key)  # Add the newly opened box to the stack
    
    # If all boxes are opened, return True
    return all(opened)

