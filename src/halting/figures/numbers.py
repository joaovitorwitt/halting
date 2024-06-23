##################################################
# Imports
##################################################
# https://packaging.python.org/en/latest/tutorials/packaging-projects/
from src.halting.base import BaseHalting

##################################################
# Significant Figures Implementation
##################################################
class ManageFigures(BaseHalting):

    def calculate_number_of_significant_figures(self, figures: str) -> int:
        """
        Significant figures are the digits of a number that are meaningful in terms of accuracy or precision.

        This function is designed to take a number, it can either be a integer or a float, 
        and return the number of significant figures, following the significant figures rules.
        Non-zero digits are always significant, zeros between non-zero digits are always significant (9009)

        Args:
            figures (str): The number formatted in string.

        Returns:
            int: The number of significant figures.

        Usage:
            >>> from src.halting.figures.numbres import ManageFigures
            >>> figures = ManageFigures()
            >>> figures.calculate_number_of_significant_figures(344.50)
            >>> 5
        """
        trailing_number_of_zeros = 0
        leading_number_of_zeros = 0

        # deal with numbers without decimal point
        try:
            if isinstance(int(figures), int):
                if '0' not in figures:
                    return len(figures)
                
                if figures[-1] == '0':
                    for number in figures[::-1]:
                        if number == '0':
                            trailing_number_of_zeros += 1
                        else:
                            break
                    return len(figures) - trailing_number_of_zeros
                
        except ValueError:
            to_list = list(figures)
            return to_list

    def scientific_notation_to_integer(self, scientific_notation: int | float) -> int | float:
        """
        Takes a scientific notation if the format: `4.4e5` and converts to its integer value.
        `4.4e5` represents `4.4 * 10 ^5`

        Args:
            scientific_notation (int | float): The number to be converted into its integer form.

        Returns:
            int | float: The formatted number now in integer or float form.

        Example:
            >>> from src.halting.figures.numbers import ManageFigures
            >>> figures = ManageFigures()
            >>> figures.scientific_notation_to_integer(5.6)
        """
        return scientific_notation
