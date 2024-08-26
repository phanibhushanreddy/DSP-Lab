import numpy as np
import matplotlib.pyplot as plt

def dtft(x, omega):
    """Compute the Discrete Time Fourier Transform (DTFT) of a signal x."""
    X = np.zeros_like(omega, dtype=complex)
    for n in range(len(x)):
        X += x[n] * np.exp(-1j * omega * n)
    return X

def main():
    # Get user input
    user_input = input("Enter the discrete-time signal values separated by spaces: ")
    try:
        # Convert the input string into a list of numbers
        x = np.array([float(value) for value in user_input.split()])
    except ValueError:
        print("Invalid input. Please enter numerical values separated by spaces.")
        return

    # Frequency range
    omega_min = -np.pi
    omega_max = np.pi
    omega_step = 0.0001 * np.pi
    omega = np.arange(omega_min, omega_max, omega_step)

    # Compute the DTFT
    X = dtft(x, omega)

    # Plot the magnitude and phase
    plt.figure(figsize=(12, 6))

    # Plot magnitude
    plt.subplot(2, 1, 1)
    plt.plot(omega, np.abs(X))
    plt.title('Magnitude of DTFT')
    plt.xlabel('Frequency (rad/sample)')
    plt.ylabel('Magnitude')
    plt.grid(True)
    plt.savefig('Magnitude.png',dpi=300)

    # Plot phase
    plt.subplot(2, 1, 2)
    plt.plot(omega, np.angle(X))
    plt.title('Phase of DTFT')
    plt.xlabel('Frequency (rad/sample)')
    plt.ylabel('Phase (radians)')
    plt.savefig('Phase.png',dpi=300)

    # Show plots
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
