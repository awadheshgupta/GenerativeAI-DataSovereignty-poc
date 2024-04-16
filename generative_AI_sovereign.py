from transformers import pipeline

def obtain_consent():
    # Simulate obtaining consent from the user
    consent = input("Do you consent to use your input for text generation? (yes/no): ")
    return consent.lower() == 'yes'

def generate_text(prompt):
    # Load a pre-trained language model
    model = pipeline("text-generation", model="gpt2")

    # Generate text based on the prompt
    generated_text = model(prompt, max_length=50, num_return_sequences=1, temperature=0.7)[0]['generated_text']
    return generated_text

def main():
    prompt = input("Enter a prompt for text generation: ")

    # Check if the user consents to use their input
    if obtain_consent():
        # Generate text using the provided prompt
        generated_text = generate_text(prompt)
        print("Generated Text:")
        print(generated_text)
    else:
        print("Without consent, unable to generate text.")

if __name__ == "__main__":
    main()
