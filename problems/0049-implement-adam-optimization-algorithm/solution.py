import numpy as np

def adam_optimizer(f, grad, x0, learning_rate=0.001, beta1=0.9, beta2=0.999, epsilon=1e-8, num_iterations=10):
	x = np.array(x0)
	m, v = np.zeros_like(x), np.zeros_like(x)

	for t in range(1, num_iterations + 1):
        g = grad(x)  # Get gradient at current position
        
        # Update biased first moment estimate
        m = beta1 * m + (1 - beta1) * g
        
        # Update biased second moment estimate
        v = beta2 * v + (1 - beta2) * (g ** 2)
        
        # Compute bias-corrected first moment estimate
        m_hat = m / (1 - beta1 ** t)
        
        # Compute bias-corrected second moment estimate
        v_hat = v / (1 - beta2 ** t)
        
        # Update parameters
        x = x - learning_rate * m_hat / (np.sqrt(v_hat) + epsilon)
    
    return x
