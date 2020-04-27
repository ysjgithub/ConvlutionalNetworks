# ConvlutionalNetworks

cite this project in your project
##### git clone https://github.com/ysjgithub/ConvlutionalNetworks.git

- use code like follow as your model
- train in cpu
- you can start with mnist dataset,run example.py
```
from ConvlutionalNetworks import Conv, Flattan, MaxPooling, SoftMax, Relu, Model

model = Model([
        Conv(1, 32, 3, 1, 1),
        Relu(),
        MaxPooling(2, 2),
        Conv(32, 64, 3, 1, 1),
        Relu(),
        MaxPooling(2, 2),
        Flattan(),
        FC(3136,96),
        Relu(),
        FC(96,10),
        Relu(),
        SoftMax()
    ])
```
