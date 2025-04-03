# lightgbm-example

### installtion
based on official LighGBM Docker instruction

```sh
$ docker build --platform linux/x86_64 \
    -t lightgbm-python \
    -f dockerfile-python \
    .
$ docker run --platform linux/x86_64 \
    --rm \
    --volume "${PWD}":/opt/training \
    --workdir /opt/training \
    lightgbm-python \
    python train.py
```

### demo
![demo](https://github.com/ryo-imai-bit/lightgbm-example/blob/master/sample.gif?raw=true)
