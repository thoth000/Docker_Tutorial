import argparse
import random
import torch
from torchvision import datasets, transforms
from model import SimpleCNN


def test(args):
    # load model
    model = SimpleCNN()
    model.load_state_dict(torch.load(args.model_path, map_location=torch.device("cpu"), weights_only=True))
    model.eval()

    # load test data
    test_data = datasets.MNIST(root=".", train=False, download=True, transform=transforms.ToTensor())

    # get random data
    index = random.randint(0, len(test_data) - 1)
    image, label = test_data[index]

    with torch.no_grad():
        output = model(image.unsqueeze(0))
        pred = output.argmax(dim=1).item()

    print(f"Index: {index}, GT: {label}, Predicted: {pred}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--model-path', type=str, default='outputs/mnist_cnn.pth')
    args = parser.parse_args()
    test(args)


if __name__ == "__main__":
    main()
