import torch
from diffusers import StableDiffusionPipeline
from PIL import Image
import os

# Initialize the Stable Diffusion model
def initialize_model(model_name="here you could put the model "):
    try:
        print("Loading the model...")
        model = StableDiffusionPipeline.from_pretrained(model_name, torch_dtype=torch.float16)
        model.to("cuda" if torch.cuda.is_available() else "cpu")
        print("Model loaded successfully!")
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        return None

# Generate an image from a text prompt
def generate_image_from_text(model, prompt, save_path="generated_image.png"):
    try:
        print(f"Generating image for prompt: {prompt}")
        with torch.no_grad():
            image = model(prompt).images[0]
            image.save(save_path)
            print(f"Image saved to {save_path}")
            return image
    except Exception as e:
        print(f"Error generating image: {e}")
        return None

# Display the generated image
def display_image(image):
    if image:
        image.show()
    else:
        print("No image to display.")

# Main function for testing
def main():
    prompt = "here you should put a sentence in order to generate the model " # sometimes it not showing a great result
    save_path = "output_image.png"

    # Initialize the model
    model = initialize_model()

    if model:
        # Generate and display the image
        generated_image = generate_image_from_text(model, prompt, save_path)
        display_image(generated_image)

if __name__ == "__main__":
    main()
