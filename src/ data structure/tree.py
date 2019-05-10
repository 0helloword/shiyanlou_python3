class Node(object):
    def __init__(self,item):
        self.item=item#表示对应的元素
        self.left=None#表示左子节点
        self.right=None#表示右子节点
    def __str__(self):
        return str(self.item)
    
class Tree(object):
    def __init__(self):
        self.root=Node('root')#根节点定义为root永不删除
        
    
    def add(self,item):
        node=Node(item)
        if self.root is None:
            self.root=node
        else:
            q=[self.root]
            while True:
                pop_node=q.pop(0)
                if pop_node.left is None:
                    pop_node.left=node
                    return
                elif pop_node.right is None:
                    pop_node.right=node
                    return
                else:
                    q.append(pop_node.left)
                    q.append(pop_node.right)
    
            
tree=Tree()
tree.add(1)
