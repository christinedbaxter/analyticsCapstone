import numpy as np

def vector_avg(angles):
    # Convert degrees to radians
    radians = np.radians(angles.dropna())

    # Calculate the mean direction using vector averaging
    mean_angle = np.arctan2(np.mean(np.sin(radians)), np.mean(np.cos(radians)))

    # Convert back to degrees and ensure the result is between 0 and 360
    mean_angle = np.degrees(mean_angle) % 360

    return mean_angle
