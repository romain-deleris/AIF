import gradio as gr
from PIL import Image
import requests
import io
import numpy as np

def recognize_digit(image):
    if image is None:
        raise gr.Error("Dessinez un chiffre avant de lancer la prédiction.")

    if isinstance(image, dict):
        image = image.get("composite")
        if image is None:
            raise gr.Error("Le dessin n'a pas pu être récupéré.")

    if image.ndim == 3:
        # The editor returns RGBA/RGB data, while the API expects one channel.
        image = image[:, :, 0]

    # invert the image
    image = 255 - image
    # convert numpy to uint8
    image = image.astype(np.uint8)
    # Convert the image to a PIL Image
    image = Image.fromarray(image)
    # Convert the image to a binary file
    img_binary = io.BytesIO()
    image.save(img_binary, format="PNG")
    # Send request to the API
    response = requests.post("http://api:5075/predict", data=img_binary.getvalue())
    return response.json()["prediction"]

if __name__=='__main__':

    interface = gr.Interface(fn=recognize_digit,
                inputs=gr.Sketchpad(
                    type="numpy",
                    image_mode="RGBA",
                    canvas_size=(280, 280),
                    fixed_canvas=True,
                    label="Dessin",
                ),
                outputs='label',
                live=False,
                description="Draw a number on the sketchpad to see the model's prediction.",
                )
    print("Starting Gradio app...")
    interface.launch(server_name="0.0.0.0", server_port=7860) # the server will be accessible externally under this address   
