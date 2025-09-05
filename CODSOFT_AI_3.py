import torch
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image

# Load pre-trained ResNet50
resnet = models.resnet50(pretrained=True)
resnet.eval()  # set to evaluation mode

# Remove the final classification layer to get features
feature_extractor = torch.nn.Sequential(*list(resnet.children())[:-1])

# Image preprocessing
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225])
])

def extract_features(img_path):
    img = Image.open(img_path).convert("RGB")
    img_t = transform(img).unsqueeze(0)  # add batch dimension
    with torch.no_grad():
        features = feature_extractor(img_t)
    return features

def generate_caption(features):
    # Dummy caption for demo (replace with trained decoder in real use)
    return "A dog is sitting on the grass."

# Example run
img_path = "dog.jpg"  # put your image here
features = extract_features(img_path)
caption = generate_caption(features)

print("Extracted feature vector shape:", features.shape)
print("Generated Caption:", caption)

