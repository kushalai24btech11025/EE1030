import matplotlib.pyplot as plt

# Define the points
A = (1/2, 3/2)
B = (2, -5)
P = (3/4, 5/12)

# Extract coordinates
x_coords = [A[0], B[0]]
y_coords = [A[1], B[1]]

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x_coords, y_coords, marker='o', label='Line Segment AB', color='blue')
plt.plot(P[0], P[1], marker='o', color='red', label='Point P')

# Annotate points
plt.text(A[0], A[1], ' A(1/2, 3/2)', fontsize=10, verticalalignment='bottom', horizontalalignment='right')
plt.text(B[0], B[1], ' B(2, -5)', fontsize=10, verticalalignment='top', horizontalalignment='left')
plt.text(P[0], P[1], ' P(3/4, 5/12)', fontsize=10, verticalalignment='bottom', horizontalalignment='right')

# Set labels and title
plt.title('Diagram of Points A, B, and P')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.xlim(0, 2.5)
plt.ylim(-6, 3)

# Show legend
plt.legend()

# Save the plot as a PNG file
plt.savefig('IMG.png')

# Display the plot
plt.show()
