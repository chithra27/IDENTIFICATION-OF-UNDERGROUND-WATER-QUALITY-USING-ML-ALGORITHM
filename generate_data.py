import numpy as np
import pandas as pd

def generate_sensor_data(num_samples=100):
    np.random.seed(42)
    pH = np.random.uniform(6.5, 8.5, num_samples)
    turbidity = np.random.uniform(0.1, 5.0, num_samples)
    conductivity = np.random.uniform(200, 1200, num_samples)
    
    labels = (pH > 7) & (turbidity < 2.5) & (conductivity < 1000)
    labels = labels.astype(int)
    
    data = pd.DataFrame({'pH': pH, 'Turbidity': turbidity, 'Conductivity': conductivity, 'Quality': labels})
    return data

data = generate_sensor_data(500)
data.to_csv("simulated_water_quality.csv", index=False)
print("Simulated data generated and saved to 'simulated_water_quality.csv'.")
