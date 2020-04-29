import numpy as np
import torchvision.datasets as datasets
import torchvision.transforms as transforms
from torch.utils.data import DataLoader
from ConvlutionalNetworks.ConvlutionalNetworks import Conv, Flattan, MaxPooling, SoftMax, Relu, Model,FC

model = Model([
        Conv(1, 6, 3, 1, 1),
        Relu(),
        MaxPooling(2, 2),
        Conv(6, 16, 3, 1, 1),
        Relu(),
        MaxPooling(2, 2),
        Conv(16, 32, 3, 1, 1),
        Relu(),
        MaxPooling(2, 2),
        Flattan(),
        FC(288,32),
        Relu(),
        FC(32,10),
        Relu(),
        SoftMax()
    ])


transform_train = transforms.Compose([
    transforms.RandomCrop(28, padding=4),
    transforms.ToTensor(),
])
transform_test = transforms.Compose([
    transforms.ToTensor(),
])

train_loader = DataLoader(
    datasets.MNIST(root='.data/mnist', train=True, download=True, transform=transform_train), batch_size=20,
    shuffle=True, num_workers=2, drop_last=True
)

test_loader = DataLoader(
    datasets.MNIST(root='.data/mnist', train=False, download=True, transform=transform_test),
    batch_size=100, shuffle=False, num_workers=2, drop_last=True
)

def one_hot(x, K):
    return np.array(x[:, None] == np.arange(K)[None, :], dtype=int)

def mytest():
    correct = 0
    for x, y in test_loader:
        x = x.numpy()
        y = one_hot(np.array(y.numpy()),10)
        s = model.forword(x)
        correct += np.sum(np.argmax(y,axis=1)==np.argmax(s,axis=1))
    print("test_correct",correct)

iter = 0
for i in range(2):
    for x,y in train_loader:
        iter+=1
        x = x.numpy()
        y = one_hot(np.array(y.numpy()),10)
        s = model.forword(x)
        r = s - y
        print(np.argmax(y,axis=1),np.argmax(s,axis=1))
        print(np.sum(np.argmax(y,axis=1)==np.argmax(s,axis=1)))
        model.backword(r)
        if iter % 1000 == 0:
            mytest()



