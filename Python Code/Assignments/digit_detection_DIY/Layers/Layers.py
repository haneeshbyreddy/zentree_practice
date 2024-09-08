import numpy as np
import random
import math

class Layers:
    def __init__(self):
        pass
    
    def apply_filter(self, image_matrix, gf):
        h1, w1 = image_matrix.shape[:2]
        h2, w2 = gf.shape[:2]

        if len(image_matrix.shape)<3:
            image_matrix = np.stack([image_matrix],-1)
        d = image_matrix.shape[2]

        new_image_matrix = np.zeros((h1-h2+1, w1-w2+1), dtype=np.uint8)
        for d in range(d):
            for i in range(h1-h2+1):
                for j in range(w1-w2+1):
                    temp = np.sum(image_matrix[i:i+h2, j:j+w2, d] * gf)
                    new_image_matrix[i, j] += temp
        return new_image_matrix
    
    def edge(self, image_matrix):
        edge = random.choice([0,1])
        if edge==0:
            fil = [[1,0,-1],[2,0,-2],[1,0,-1]]
        else:
            fil = [[1,2,1],[0,0,0],[-1,-2,-1]]
        return self.apply_filter(image_matrix, np.array(fil))
        
    def laplacian(self, image_matrix):
        fil = [[0,-1,0],[-1,4,-1],[0,-1,0]]
        return self.apply_filter(image_matrix, np.array(fil))

    def gaussian(self, image_matrix):
        size = 3
        sigma = round(random.random(),1)+0.1
        func = lambda x, y : (1/(2*np.pi*sigma**2)) * np.exp(-((x-(size-1)/2)**2 + (y-(size-1)/2)**2) / (2*sigma**2))
        kernal = np.zeros((size,size))
        for i in range(size):
            for j in range(size):
                kernal[i][j] = func(i, j)
        kernal /= np.sum(kernal)
        return self.apply_filter(image_matrix, kernal)

    def conv(self, image_matrix, n):
        output = []
        funcs = [self.gaussian, self.laplacian, self.edge]
        random.seed(10)

        for _ in range(n):
            output.append(funcs[math.floor(random.random()*len(funcs))](image_matrix))
        return np.stack(output, -1)

    def maxpool(self, image_matrix, maxpoll=2):
        h1, w1 = image_matrix.shape[:2]

        if len(image_matrix.shape)<3:
            image_matrix = np.stack([image_matrix],-1)

        d = image_matrix.shape[2]
        new_image_matrix = np.zeros((h1-maxpoll+1, w1-maxpoll+1,d), dtype=np.uint8)
        for d in range(d):
            for i in range(h1-maxpoll+1):
                for j in range(w1-maxpoll+1):
                    temp = np.max(image_matrix[i:i+maxpoll, j:j+maxpoll, d])
                    new_image_matrix[i, j, d] = temp
        return new_image_matrix
    
    def relu(self, image_matrix):
        return np.maximum(0, image_matrix)
    
    def flatten(self, image_matrix):
        return np.array([image_matrix.flatten()])
    
    def fc(self, image_matrix, weights):
        output = image_matrix @ weights
        return output
    
    def softmax(self, x, temparature=1):
        x = x / temparature
        e = np.exp(x - np.max(x))
        return e / np.sum(np.exp(e))
    
    def loss_function(self, final, expected):
        return (final - expected)**2/len(final)
    
    def apply_stacks(self, img, stacks):
        for i in stacks:
            stack = self.conv(np.array(img), i)
            stack_maxpool = self.maxpool(stack)
            stack_relu = self.relu(stack_maxpool)
            img = stack_relu
        return img
    
    def apply_fc(self, img, weights):
        output = img
        self.act_out = []
        for i in weights:
            fc_out = self.fc(output, i)
            if i.shape != weights[-1].shape:
                fc_relu = self.relu(fc_out)
            else:
                fc_relu = fc_out
            output = fc_relu
            self.act_out.append(output)
        return output
    
    def dl_dw(self, final, label):
        learning_rate = 0.01
        gradients = []
        error = final - label

        self.back_weights
        self.act_out

        return gradients



    
    def backtrack(self, images, labels, stacks, fc_weights):
        self.back_weights = []
        changes = []

        for i in range(len(fc_weights)-1):
            self.back_weights.append(np.random.rand(fc_weights[i], fc_weights[i+1]) * 2 - 1)
            changes.append(np.zeros((fc_weights[i], fc_weights[i+1])))
        
        for i in range(len(images)):
            label = [0 if labels[0] != i else 1 for i in range(10)]
            img_s = self.apply_stacks(images[i], stacks)
            flat = self.flatten(img_s)
            output = self.apply_fc(flat, self.back_weights)
            final = self.softmax(output)
            changes += self.dl_dw(final, label)

        return self.back_weights + changes