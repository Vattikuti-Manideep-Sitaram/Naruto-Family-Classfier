
# Naruto or Boruto or Minato Classifier

Welcome to the village hidden in the GPU. This project trains a fastai vision model that can tell if a picture features Naruto Uzumaki, Boruto Uzumaki, or Minato Namikaze. Feed it your favorite frames, fan-art, or memes and it will yell the right Hokage name faster than Naruto can say "dattebayo".

## TL;DR (Too Long; Dattebayo!)
- One-stop classifier for the most chaotic ninja family.
- Ships with a Gradio interface so you can share it with your squad instantly.
- Exported `model.pkl` lets you drop the brain straight into any fastai-powered deployment.

## How the jutsu works
- **Training dojo:** fastai `vision_learner` fine-tuned on curated images of Naruto, Boruto, and Minato.
- **Augmentations:** flips, rotations, lighting chaos, and a sprinkle of ninja smoke to keep the model sharp.
- **Interface:** `gradio_interface.py` powers a simple upload-and-predict UI.
- **Export:** `model.pkl` (and `export1.pkl` if you prefer) contains the trained weights ready for inference.

## Summon the classifier
1. Create a virtual environment: `python -m venv venv && venv/Scripts/activate`
2. Install dependencies: `pip install -r requirements.txt`
3. Launch the app: `python gradio_interface.py`
4. Drop in an image, wait for the chakra to flow, admire the prediction.

## Legendary quotes to keep morale high
> "Naruto: I never go back on my word. That is my nindo... and also why this README is extra long."
>
> "Boruto: Dad, did you seriously train a classifier to keep spying on me?"
>
> "Minato: I sealed the Nine-Tails, I can definitely seal this model into a pickle file."
>
> "Kakashi (probably): Remember kids, even Sharingan can't beat good data augmentation."

## Project map
- `gradio_interface.py` - Launches the Gradio UI and downloads the exported learner if needed.
- `model.pkl` / `export1.pkl` - fastai learners with all the Hokage know-how baked in.
- `main.ipynb` - end-to-end training notebook (data prep, fine-tune, export).
- `model_pkl_test.ipynb` - sanity checks and inference experiments.
- `naruto_or_boruto_or_minato/` - helper scripts and dataset utilities.

## Tips for further training arc
- Add Sarada, Himawari, or Jiraiya classes for a full Uzumaki extended universe.
- Swap the backbone to a ViT and call it "Sage Mode Transformer".
- Deploy on Hugging Face Spaces or a Discord bot so predictions can interrupt your friends at 3 AM.

## Credits and ramen fund
All Naruto assets belong to their original creators. Please support the official release, tip your fan artists, and send ramen coupons to Ichiraku.

Pull requests welcome, as long as you drop at least one Naruto quote in the description.
