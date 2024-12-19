import numpy as np

class Node(object):
	def __init__(self,x,y,value):
		self.x = x
		self.y = y
		self.value = value
	def printInfo(self):
		print(self.x,self.y,self.value)


def getAtomsphericLight(darkChannel, img):
    img = np.float32(img)
    height = darkChannel.shape[0]
    width = darkChannel.shape[1]
    nodes = []

    for i in range(0, height):
        for j in range(0, width):
            oneNode = Node(i, j, darkChannel[i, j])
            nodes.append(oneNode)
    
    nodes = sorted(nodes, key=lambda node: node.value, reverse=False)
    # print('nodes[0]',nodes[0].value)
    # print('img[nodes[0].x, nodes[0].y, 0]+img[nodes[0].x, nodes[0].y, 1])',img[nodes[0].x, nodes[0].y, 0],img[nodes[0].x, nodes[0].y, 1])
    atomsphericLight  = np.mean([img[nodes[0].x, nodes[0].y, 0],img[nodes[0].x, nodes[0].y, 1]])
    atomsphericLightGB = img[nodes[0].x, nodes[0].y, 0:2]
    atomsphericLightRGB = img[nodes[0].x, nodes[0].y, :]
    # atomsphericLight  =  [img[nodes[0].x, nodes[0].y, 0],img[nodes[0].x, nodes[0].y, 1]]
    return atomsphericLight,atomsphericLightGB,atomsphericLightRGB
