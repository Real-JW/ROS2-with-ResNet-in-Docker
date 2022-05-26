from torchvision import models
import cv2 as cv
import torch
from torchvision import transforms

def imageRead():
  transform = transforms.Compose([            #[1]
  transforms.ToTensor(),                     #[4]
  transforms.Normalize(                      #[5]
  mean=[0.485, 0.456, 0.406],                #[6]
  std=[0.229, 0.224, 0.225]                  #[7]
  )])

  cap = cv.VideoCapture(0)

  with open('imagenet_classes.txt') as f:
    labels = [line.strip() for line in f.readlines()]

  dir(models)

  resnet = models.resnet18(pretrained=True)

  resnet.eval()

  while(True):
      # Capture frame-by-frame
      ret, frame = cap.read()

      img_t = transform(frame)
      batch_t = torch.unsqueeze(img_t, 0)

      preds = resnet(batch_t)
      pred, class_idx = torch.max(preds, dim=1)
      print(labels[class_idx])

      if cv.waitKey(1) & 0xFF == ord('q'):
        break

  cap.release()
  cv.destroyAllWindows()

if __name__ == '__main__':
    imageRead()