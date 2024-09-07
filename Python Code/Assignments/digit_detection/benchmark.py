import torch
import time

def matrix_multiplication(device, size):
    # Generate random matrices
    mat1 = torch.rand(size, size, device=device)
    mat2 = torch.rand(size, size, device=device)

    # Start the timer
    start_time = time.time()

    # Perform matrix multiplication
    result = torch.matmul(mat1, mat2)

    # End the timer
    end_time = time.time()

    # Calculate the time taken
    time_taken = end_time - start_time
    return time_taken

def main():
    size = 10000  # Size of the matrices

    # Run on CPU
    print("Running on CPU...")
    cpu_time = matrix_multiplication(device='cpu', size=size)
    print(f"Time taken on CPU: {cpu_time:.4f} seconds")

    # Run on GPU (Metal backend for Mac)
    if torch.backends.mps.is_available():
        print("Running on GPU (MPS)...")
        gpu_time = matrix_multiplication(device='mps', size=size)
        print(f"Time taken on GPU (MPS): {gpu_time:.4f} seconds")
    else:
        print("GPU (MPS) is not available. Ensure you have the right PyTorch version and MacOS support.")

if __name__ == "__main__":
    main()
