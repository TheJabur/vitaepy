# ============================================================================ #
# helper_functions.py
# CV Python helper functions, accessible in jinja2 templates.

from datetime import datetime
from dateutil.parser import parse


class HelperFunctions():

# ============================================================================ #
# year
    def year(date_string: str) -> str:
        """
        Accepts a string that has a date in some format and returns the year as a string.

        Args:
            date_string: The string containing the date.

        Returns:
            A string representing the year (e.g., "2023"), or None if the date cannot be parsed.
        """
        if not isinstance(date_string, str):
            print("Input must be a string.")
            return None

        try:
            dt_object = parse(date_string, fuzzy=True)
            return str(dt_object.year)
        except ValueError:
            print(f"Could not parse date string: '{date_string}'")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None
        

# ============================================================================ #
# years
    def years(date_start=None, date_end=None):
        """
        Accepts a start date and an end date and outputs a formatted string representing the year range.

        Args:
            date_start: The start date string, or None.
            date_end: The end date string, or None.

        Returns:
            A string formatted as 'YYYY - YYYY', 'YYYY -     ', or '     - YYYY'.
        """

        date_start = date_start.strip() or None # "" is falsy
        date_end = date_end.strip() or None

        start_year_str = HelperFunctions.year(date_start) if date_start is not None else None
        end_year_str = HelperFunctions.year(date_end) if date_end is not None else None

        # Determine the left side of the string
        left_side = start_year_str or '&nbsp;'*8 # YYYY ~ 8 spaces (font dep.)

        # Determine the right side of the string
        right_side = end_year_str or '&nbsp;'*8

        return f"{left_side} - {right_side}"

 
# ============================================================================ #
# fullName
    def fullName(first: str, last: str, middle=None):
        """
        Takes first, last and optionally middle names and formats together.
        """

        initial = middle[0] if middle else ""
    
        full_name = f"{first} {initial}. {last}".title()

        return full_name


# ============================================================================ #
# entryWithID
    def entryWithID(subData, id):
        """
        First entry in sub data (e.g. personal) that has given id.
        """

        return next((d for d in subData if d['id'] == id), None)


# ============================================================================ #
# version
    def version():
        """
        """

        return datetime.now().strftime("%Y-%m-%d")
