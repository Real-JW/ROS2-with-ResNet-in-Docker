## First, run the Dockerfile to build the image;
```bash
sudo docker build -t resnet .
```


## Then, run the image to finish the task.

```bash
sudo docker run -it --rm --device=/dev/video0 -e DISPLAY=unix$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix resnet
```
