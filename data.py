!pip install matplotlib.pyplot as plt

qualities = []
expected_val = []
actual_val = []

def create_graph():
  plt.figure(figsize=(8,5))
  plt.plot(qualities, expected_val, marker='o', linestyle=' -', color='blue', label='Expected')
  plt.plot(qualities, actual_val, marker='o', linestyle=' -', color='orange', label='Actual')

  #connect dots with lines later

  plt.ylabel('Proportion')
  plt.ylim(0,1)
  plt.title('Expected ESS vs Actual Output')
  plt.legend()
  plt.grid(alpha=0.3)

  plt.show()
