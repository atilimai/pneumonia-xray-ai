## Demo Technology Decision (#91)

For the interactive demonstration of our Pneumonia Detection model, the team has agreed to use **Gradio**.

### Why Gradio?
* **Lightweight & Fast:** Gradio allows us to quickly build a web-based UI for our PyTorch/Hugging Face models with minimal boilerplate code.
* **Hosting Compatibility:** It is natively supported by Hugging Face Spaces, which is our planned hosting platform for the demo.
* **Image & Heatmap Support:** It easily handles medical image uploads and can perfectly display our Grad-CAM heatmap overlays side-by-side with the original X-rays.
* **Python-Native:** Requires no separate frontend development (HTML/CSS/JS); everything is written in Python, matching our team's existing skill set and environment.

This decision satisfies the requirements for a lightweight, interactive demo as outlined in the project planning phase.
