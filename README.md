# 🧠 User Story Domain Classifier

[![Hugging Face Transformers](https://img.shields.io/badge/HuggingFace-Transformers-yellow)](https://huggingface.co/transformers/)
[![PyTorch](https://img.shields.io/badge/PyTorch-Model-red)](https://pytorch.org/)
[![Gradio UI](https://img.shields.io/badge/Gradio-Live%20Demo-005BBB)](https://gradio.app/)
[![Colab](https://img.shields.io/badge/Open%20in-Colab-yellow.svg)](https://colab.research.google.com/github/<your-username>/<your-repo>/blob/main/UserStory_Classifier.ipynb)

A **DistilBERT-based NLP classifier** that automatically identifies the **domain or intent** of agile-style user stories. This helps teams **organize**, **understand**, and **prioritize** product backlogs.

---

## 🧭 Domains Supported

- E-commerce  
- Fitness  
- Task Management  
- News  
- Billing  
- Education  
- And more...

---

## 🎯 Project Goal

To build a lightweight, accurate classifier that categorizes user stories into **relevant domains** using NLP, improving:

- Product backlog organization  
- Feature prioritization  
- User intent understanding  

---

## 🧠 Model Details

- **Base Model**: `distilbert-base-uncased`  
- **Fine-Tuned With**: HuggingFace Transformers  
- **Accuracy**: >90% on custom test prompts  
- **Dataset**: Balanced, manually labeled  
- **UI**: Real-time Gradio interface for testing

---

## 🚀 How to Run (Google Colab)

### 📁 Files Needed

- `UserStory_Classifier.ipynb`
- `saved_model.zip` (DistilBERT weights + tokenizer)
- `label_encoder.pkl` (for decoding predictions)

### 🧪 Steps

1. Open `UserStory_Classifier.ipynb` in [Google Colab](https://colab.research.google.com/)
2. Click **Runtime → Run all** or press `Ctrl + F9`
3. When prompted, upload:
   - `saved_model.zip`
   - `label_encoder.pkl`
4. Use the **Gradio UI** to enter your own user stories and see predictions.

---

## 💡 Example Inputs

> “As a user, I want to track my steps and calories.”  
> 🟢 **Predicted Domain**: `Fitness`

> “As a user, I want to review the items I ordered.”  
> 🟢 **Predicted Domain**: `E-commerce`

---

## 🛠 Tech Stack

| Tool            | Purpose                                 |
| --------------- | --------------------------------------- |
| 🤗 Transformers | Pre-trained language modeling           |
| PyTorch         | Model training backend                  |
| Gradio          | Web UI for real-time testing            |
| pandas          | Data manipulation                       |
| scikit-learn    | Label encoding, train-test split        |

---

## 👥 Authors

- **Neha Raj C**  
- **Dheeraj**  

Special thanks to our team for manual data labeling and validation!

---

## 📝 Notes

This notebook is cleaned and simplified for demonstration purposes. For full training scripts or expanded datasets, feel free to contribute or raise an issue.

---

⭐️ **Star this repo** if you found it useful!  
📬 **Contributions & Issues Welcome**

