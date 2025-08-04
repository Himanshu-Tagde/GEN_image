
import replicate
import requests

# Initialize Replicate client with your API token
client = replicate.Client(api_token="000000000")  #  Replace with your real token

# Open your input image
with open("face2.jpg", "rb") as image_file:  
    output = client.run(
        "black-forest-labs/flux-dev",
        input={
            "image": image_file,
            "prompt": "Same beautiful girl standing in new york city, ultra realistic, DSLR quality",
            "go_fast": True,
            "guidance": 3.5,
            "megapixels": "1",
            "num_outputs": 1,
            "aspect_ratio": "1:1",
            "output_format": "webp",
            "output_quality": 80,
            "prompt_strength": 0.8,
            "num_inference_steps": 28
        }
    )

# Save the output image
image_url = output[0]
image_data = requests.get(image_url).content
with open("generated_flux_image2.webp", "wb") as f:
    f.write(image_data)

print("✅ Image saved as: generated_flux_image.webp")
