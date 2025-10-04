from fastai.vision.all import *
import gradio as gr

# Load the trained model
learn = load_learner("model.pkl")

# Prediction function (only class name)
def predict(img):
    pred_class, pred_idx, probs = learn.predict(img)
    return str(pred_class)   # return just the class name

# Gradio interface
image_input = gr.Image(type="pil")
label_output = gr.Label(num_top_classes=1)  # only top class

demo = gr.Interface(
    fn=predict,
    inputs=image_input,
    outputs=label_output,
    title="FastAI Image Classifier",
    description="Upload an image and get the predicted class name"
)

# Run inside Jupyter
demo.launch(share=True)
