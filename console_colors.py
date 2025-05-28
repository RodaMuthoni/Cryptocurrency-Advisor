"""
Console colors module for enhancing terminal output.
Provides ANSI color codes for formatting text in the terminal.
"""

# ANSI color codes for terminal output
COLORS = {
    'RESET': '\033[0m',
    'BOLD': '\033[1m',
    'UNDERLINE': '\033[4m',
    'BLACK': '\033[30m',
    'RED': '\033[31m',
    'GREEN': '\033[32m',
    'YELLOW': '\033[33m',
    'BLUE': '\033[34m',
    'MAGENTA': '\033[35m',
    'CYAN': '\033[36m',
    'WHITE': '\033[37m',
    'BG_BLACK': '\033[40m',
    'BG_RED': '\033[41m',
    'BG_GREEN': '\033[42m',
    'BG_YELLOW': '\033[43m',
    'BG_BLUE': '\033[44m',
    'BG_MAGENTA': '\033[45m',
    'BG_CYAN': '\033[46m',
    'BG_WHITE': '\033[47m',
}

def colorize(text, color_code):
    """
    Add color to text using ANSI color codes.
    
    Args:
        text (str): The text to colorize
        color_code (str): The color code from the COLORS dictionary
        
    Returns:
        str: Colorized text
    """
    return f"{COLORS.get(color_code, '')}{text}{COLORS['RESET']}"

def bold(text):
    """Make text bold."""
    return colorize(text, 'BOLD')

def green(text):
    """Make text green."""
    return colorize(text, 'GREEN')

def red(text):
    """Make text red."""
    return colorize(text, 'RED')

def yellow(text):
    """Make text yellow."""
    return colorize(text, 'YELLOW')

def blue(text):
    """Make text blue."""
    return colorize(text, 'BLUE')

def cyan(text):
    """Make text cyan."""
    return colorize(text, 'CYAN')

def magenta(text):
    """Make text magenta."""
    return colorize(text, 'MAGENTA')