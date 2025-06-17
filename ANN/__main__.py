import numpy as np
import random

# ReLU activation function
def relu(x):
    return max(0, x)

# Derivative of ReLU
def relu_derivative(x):
    return 1 if x > 0 else 0

# Function to compute the output of the perceptron
def execute_pe(input1, w1, input2, w2, b1):
    net = (input1 * w1) + (input2 * w2) + b1
    return relu(net)

def train_ann(inputs, targets, w1_init, w2_init, b1_init, learn_rate, epoch_target, target_error, training_type=1):
    """
    Trains a simple ANN with ReLU using:
    training_type = 1: SGD
    training_type = 2: Mini-batch SGD (not implemented differently here)
    training_type = 3: Batch GD
    """
    w1, w2, b1 = w1_init, w2_init, b1_init
    epoch = 0
    error = 1.0
    num_patterns = len(inputs)

    if training_type in [1, 2]:  # SGD / Mini-batch SGD
        while epoch < epoch_target and error > target_error:
            for i in range(num_patterns):
                input1, input2 = inputs[i]
                target = targets[i]

                output = execute_pe(input1, w1, input2, w2, b1)
                error = 0.5 * (target - output) ** 2

                dE_dOut = output - target
                dOut_dNet = relu_derivative(output)

                # Gradients
                dE_dW1 = dE_dOut * dOut_dNet * input1
                dE_dW2 = dE_dOut * dOut_dNet * input2
                dE_dB = dE_dOut * dOut_dNet * 1

                # Update weights
                w1 -= learn_rate * dE_dW1
                w2 -= learn_rate * dE_dW2
                b1 -= learn_rate * dE_dB

                epoch += 1

                if error <= target_error or epoch >= epoch_target:
                    break

    else:  # Batch Gradient Descent
        while error > target_error and epoch < epoch_target:
            error = 0.0
            dw1_total = dw2_total = db_total = 0.0

            for i in range(num_patterns):
                input1, input2 = inputs[i]
                target = targets[i]

                output = execute_pe(input1, w1, input2, w2, b1)
                dE_dOut = output - target
                dOut_dNet = relu_derivative(output)

                dw1_total += dE_dOut * dOut_dNet * input1
                dw2_total += dE_dOut * dOut_dNet * input2
                db_total += dE_dOut * dOut_dNet * 1

                error += 0.5 * (target - output) ** 2

            # Update weights with average gradient
            w1 -= learn_rate * dw1_total / num_patterns
            w2 -= learn_rate * dw2_total / num_patterns
            b1 -= learn_rate * db_total / num_patterns

            epoch += 1

            if error > 100:
                print(f"Warning: Exploding error! ({error}) — consider lowering the learning rate.")
                answer = input("Do you want to terminate training? (yes/no): ")
                if answer.lower() == "yes":
                    break

    return w1, w2, b1, epoch, error


if __name__ == "__main__":
    # Sample training data (each tuple: input1, input2)
    inputs = [
        (-1.0, -1.0),
        (-1.0, 1.0),
        (1.0, -1.0),
        (1.0, 1.0)
    ]

    # Corresponding target outputs = NAND gate
    targets = [1.0, 1.0, 1.0, -1.0]

    # Initial weights and bias
    w1_init = random.uniform(-1, 1)
    w2_init = random.uniform(-1, 1)
    b1_init = random.uniform(-1, 1)

    print(f"Initial Weights: W1 = {w1_init:.4f}, W2 = {w2_init:.4f}, B1 = {b1_init:.4f}")

    # Training parameters
    learn_rate = 0.01
    epoch_target = 10000
    target_error = 0.001

    # Type: 1 = SGD, 2 = Mini-batch SGD, 3 = Batch GD
    training_type = 3

    # Train the model
    w1, w2, b1, epochs_done, final_error = train_ann(
        inputs, targets,
        w1_init, w2_init, b1_init,
        learn_rate, epoch_target, target_error,
        training_type
    )

    # Show final results
    print(f"\nTrained in {epochs_done} epochs")
    print(f"Final Weights: W1 = {w1:.4f}, W2 = {w2:.4f}, B1 = {b1:.4f}")
    print(f"Final Error: {final_error:.6f}\n")

    # Test Inputs
    for input1, input2 in inputs:
        output = execute_pe(input1, w1, input2, w2, b1)
        print(f"Input: ({input1}, {input2}) → Output: {output:.4f}")
