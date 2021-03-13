"""Keypress - A module for detecting a single key press"""

try:
    import msvcrt

    def getkey():
        """Wait for a keypress and return a single character."""

        return msvcrt.getch()

except ImportError:

    import sys
    import tty
    import termios

    def getkey():
        """Wait for a keypress and return a single character."""

        fd = sys.stdin.fileno()

        original_attributes = termios.tcgetattr(fd)
         
        try:
            tty.setraw( sys.stdin.fileno() )
            ch = sys.stdin.read(1)
        finally:
            termios,tcsetattr(fd, termios.TCSADRAIN, original_attributes  )
            
        return ch


    # If either of the Unix-specific tty or termios are not found,
    # we allow the ImportError to propagate from here to the caller.