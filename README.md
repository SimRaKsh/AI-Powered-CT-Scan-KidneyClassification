## Smart Kidney: AI-Powered CT Scan Classification System

Smart Kidney is an AI-powered medical imaging system that analyzes kidney CT scan images and classifies them into four categories:
-Cyst
-Tumor
-Stone
-Normal
The system combines a Next.js + TailwindCSS frontend with a Flask + PyTorch backend, delivering real-time inference using a deep learning model trained on medical CT images.

This project demonstrates full-stack development, model integration, image preprocessing, REST API design, and deployment using modern web technologies.

### Frontend URL: https://kidney-disease-classification.vercel.app/
### Backend URL: 
- (Model Notebooks can be found in Research Folder)
- (Model Results can be found in Results Folder)

## Features
- Upload CT images from browser
- Real-time AI inference using PyTorch
- Smooth UI built using Next.js TailwindCSS & Flowbite
- Dynamic theme with dark-mode support
- Flask REST API for image classification
- Integrated preprocessing pipeline (Resize → CenterCrop → Normalize)
- Full-stack architecture (frontend + backend)

## Technology Stack
### Frontend:
- Nextjs 14
- React
- TypeScript
- TailwindCSS
- Flowbite / Flowbite-React
### Backend:
- Python
- Flask
- Flask-CORS
- PyTorch
- TorchVision
- TIMM
- Pillow

## Models Information
The model is based on the EfficientViT-M2 architecture, fine-tuned on a publicly available kidney CT scan dataset.
### Classes:
- Cyst
- Tumor
- Stone
- Normal
### Input Preprocessing
- Resize → 256
- CenterCrop → 224
- ToTensor
- Normalize with ImageNet means/std

## Project Structure
Smart-Kidney/
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── best_model/
│       └── efficientvit_m2_kidney_disease_classifier.pth
│
├── frontend/
│   ├── app/
│   ├── components/
│   ├── public/
│   ├── styles/
│   ├── package.json
│   └── tailwind.config.ts
│
└── README.md

# How to run Backend?
### STEPS:

Clone the repository

```bash
git clone https://github.com/Prriyanshu9898/Kidney-Disease-Classification-Using-Deep-Learning.git
```
### STEP 01- Create a Python environment after opening the repository

```bash
cd Kidney-Disease-Classification-Using-Deep-Learning
python -m venv env
```

```bash
env\Scripts\activate
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```
### STEP 03- Run the Flask Backend
```bash
python app.py
```
### STEP 04- Run the Training Pipeline
```bash
python main.py
```

# How to run Frontend?
### STEP 01- Go to client
```bash
cd frontend
```
### STEP 02- install the requirements
```bash
npm install
```

### STEP 03- Run the NextJS frontend
```bash
npm run dev
```

### STEP 04- Build the frontend
```bash
npm run build
```

## Deployment
### Frontend Deployment
- Use Vercel
- Auto-deploy on pushes to main branch
### Backend Deployment
Use Render
- Create a new Web Service
- Set app.py as entry
- Add requirements.txt
- Start command:
```bash
gunicorn app:app

```
After deployment, update the frontend Axios URL.

## Dataset Source
CT Kidney Dataset
- Normal
- Cyst
- Tumor
- Stone
Kaggle link:
https://www.kaggle.com/datasets/nazmul0087/ct-kidney-dataset-normal-cyst-tumor-and-stone

## License
This project is for educational and research purposes.
