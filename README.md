---
title: Naruto Family Classifier
emoji: 🌍
colorFrom: gray
colorTo: green
sdk: gradio
sdk_version: 5.49.0
app_file: app.py
pinned: false
license: apache-2.0
short_description: Classifies Naruto, Boruto, Minato Images
---

# Naruto or Boruto or Minato Classifier

![Naruto celebrates ramen victory](https://media4.giphy.com/media/itJhWF0zY5zcY/giphy.gif)

Believe it! This repo trains a cheeky little model that looks at a single frame of anime glory and shouts whether it spotted Naruto, Boruto, or Minato. It is powered by fastai and wrapped in a Gradio app so your friends can spam meme images until the Hokage Tower collapses.

## Why you might summon this jutsu
- Rapid-fire character ID for your stash of reaction gifs
- Ramen shop loyalty program verification (Naruto only, sorry Boruto)
- Shrugs off low-effort cosplay shots faster than Kakashi late to class

## Gallery of Goofs
![Boruto caught skipping training](https://media3.giphy.com/media/CWj2gGZbfV1igevrmY/giphy.gif)
![Minato speed-running bedtime stories](https://media1.giphy.com/media/3ov9jP09WyYr2G4OY8/giphy.gif)

## Quick start
1. Create an environment: <code>python -m venv venv && venv/Scripts/activate</code>
2. Install the goods: <code>pip install -r requirements.txt</code>
3. Launch the Gradio portal: <code>python app.py</code>
4. Drop in an image and let the model flex its chakra control.

## Model ramen notes
- Based on a fastai <code>vision_learner</code> fine-tuned on a handcrafted Naruto family dataset.
- Training tips: rely on heavy augmentations (flip, warp, contrast) so the model laughs at dramatic lighting.
- Feel free to fine-tune with your own clan portraits by swapping out the image folder path and re-running the notebook.

## Project structure cheat sheet
- <code>app.py</code> – Gradio UI, auto-downloads the exported learner.
- <code>export.pkl</code> – Fastai learner with all the sage wisdom baked in.
- <code>requirements.txt</code> – Everything you need except Ichiraku coupons.
- <code>01_intro.ipynb</code>, <code>main.ipynb</code>, <code>model_pkl_test.ipynb</code> – Notebooks for training, testing, and poking the model with kunai.

## Deploy like a shinobi
- Hugging Face Space friendly (see front-matter on top).
- GitHub ready: you can ship to any cloud ninja village that reads a <code>requirements.txt</code>.
- For Docker fans, grab the dependencies and expose <code>7860</code> for a quick summoning ritual.

## Upgrade ideas
- Add Sarada so someone finally keeps Boruto honest.
- Swap the backbone to a vision transformer and call it "Sage Mode".
- Build a Discord bot that posts Minato only when the chat needs dad jokes.

## Credits
Made with respect to the Naruto franchise. All gifs belong to their respective creators; consider tossing them some ramen money.

Pull requests welcome—just keep them funnier than Naruto's shadow clone stand-up routine.
