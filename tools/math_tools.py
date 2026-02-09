def calculate_percentage(part: float, whole: float) -> str:
    """Calculates what percentage 'part' is of 'whole'."""
    if whole == 0:
        return "Error: Division by zero."
    percentage = (part/whole) * 100
    return f"{part} is {percentage:.2f}% of {whole}"
