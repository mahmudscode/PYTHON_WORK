def calculate_cgpa(grades, credits):
    """
    Calculate CGPA (Cumulative Grade Point Average).
    
    Args:
        grades: List of grade points (0-4.0 scale)
        credits: List of credit hours for each course
    
    Returns:
        float: CGPA rounded to 2 decimal places
    """
    if len(grades) != len(credits):
        raise ValueError("Grades and credits lists must have same length")
    
    if sum(credits) == 0:
        raise ValueError("Total credits cannot be zero")
    
    total_grade_points = sum(g * c for g, c in zip(grades, credits))
    total_credits = sum(credits)
    
    cgpa = total_grade_points / total_credits
    return round(cgpa, 2)


# Example usage
if __name__ == "__main__":
    grades = [3.8, 3.5, 4.0, 3.2]  # Grade points
    credits = [3, 4, 3, 4]           # Credit hours
    
    cgpa = calculate_cgpa(grades, credits)
    print(f"CGPA: {cgpa}")