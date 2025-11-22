from flask import Flask, request, jsonify
from flask_cors import CORS
import torch
from torchvision import transforms
import timm
from PIL import Image
from io import BytesIO
import base64

app = Flask(__name__)
CORS(app)

def load_model(model_name, num_classes, device):
    model = timm.create_model(model_name, pretrained=False, num_classes=num_classes)
    model_path = 'best_model/efficientvit_m2_kidney_disease_classifier.pth'
    model.load_state_dict(torch.load(model_path, map_location=device))
    model.to(device)
    model.eval()
    return model

def preprocess_image(image):
    transform = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                             std=[0.229, 0.224, 0.225]),
    ])
    return transform(image).unsqueeze(0)

@app.route('/')
def index():
    return "<h1>Kidney Disease Detector Backend</h1>"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        base64_str = data['image']

        # Remove data:image/jpeg;base64, part if it exists
        if "," in base64_str:
            base64_str = base64_str.split(",")[1]

        image = Image.open(BytesIO(base64.b64decode(base64_str))).convert('RGB')

        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        model = load_model('efficientvit_m2', 4, device)
        tensor = preprocess_image(image).to(device)

        with torch.no_grad():
            outputs = model(tensor)
            _, pred = torch.max(outputs, 1)

        labels = ['Cyst', 'Tumor', 'Stone', 'Normal']
        result = labels[pred.item()]

        return jsonify({'prediction': result})
    except Exception as e:
        print("🔥 Error:", e)
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
