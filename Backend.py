import math

def calculate_color_similarity(r1, g1, b1, r2, g2, b2):
    # Normalize RGB values to range 0-1
    r1, g1, b1 = r1/255, g1/255, b1/255
    r2, g2, b2 = r2/255, g2/255, b2/255

    # Calculate Euclidean distance
    distance = math.sqrt((r1 - r2)**2 + (g1 - g2)**2 + (b1 - b2)**2)

    # Convert distance to similarity percentage
    max_distance = math.sqrt(3)  # Maximum possible distance in RGB color space
    similarity = (1 - distance / max_distance) * 100

    return round(similarity, 2)

# Example usage:
r1 = int(input("Enter R value for color 1: "))
g1 = int(input("Enter G value for color 1: "))
b1 = int(input("Enter B value for color 1: "))
r2 = int(input("Enter R value for color 2: "))
g2 = int(input("Enter G value for color 2: "))
b2 = int(input("Enter B value for color 2: "))

similarity = calculate_color_similarity(r1, g1, b1, r2, g2, b2)
print(f"Color similarity: {similarity}%")