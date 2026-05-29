## Demo Input/Output Interface Definition 

The interactive demonstration interface built with Gradio will follow a structured input-to-output workflow to ensure a seamless user experience for evaluating the Pneumonia Detection model.

### 1. Input Component
* **Image Upload:** A drag-and-drop file uploader (`gr.Image`) that accepts a single chest X-ray image (supported formats: PNG, JPG, JPEG).

### 2. Output Components
The interface will return three distinct outputs after processing the input image:
* **Classification Label:** Displays whether the model detects **Pneumonia** or **Normal**.
* **Confidence Score:** Displays the probability percentage (e.g., 94.5%) showing the certainty of the prediction.
* **Grad-CAM Overlay:** An image output showing the original X-ray overlaid with a Grad-CAM heatmap visualization to highlight the specific lung regions the model focused on.
