#include <bits/stdc++.h>

#ifndef BINARY_TREE
#define BINARY_TREE

namespace algo
{
    template <typename T>
    class BinaryTree
    {
    public:
        BinaryTree() = delete;
        ~BinaryTree() { delete _root; }

        struct Generator
        {
            static BinaryTree<T> *generateWithPreAndInOrder(std::vector<T> preOrder, std::vector<T> inOrder);
            static BinaryTree<T> *generateWithPreAndInOrder(T preOrder[], T inOrder[], int size);
            static BinaryTree<T> *generateWithPostAndInOrder(std::vector<T> postOrder, std::vector<T> inOrder);
            static BinaryTree<T> *generateWithPostAndInOrder(T postOrder[], T inOrder[], int size);
        };

        std::vector<T> traversePreOrder();
        std::vector<T> traverseInOrder();
        std::vector<T> traversePostOrder();

    private:
        struct Node
        {
            Node(T data) : _data(data){};
            Node(T data, Node left, Node right) : _data(data), _right(&right), _left(&left){};
            Node(T data, Node *left, Node *right) : _data(data), _right(right), _left(left){};
            ~Node()
            {
                if (_left != nullptr)
                    delete _left;
                if (_right != nullptr)
                    delete _right;
            }

            const T &getData() { return _data; }
            void setData(T data) { _data = data; }

            const Node *getLeftNode() { return _left; }
            void setLeftNode(Node *left) { _left = left; }
            void setLeftNode(Node left) { _left = &left; }

            const Node *getRightNode() { return _right; }
            void setRightNode(Node *right) { _right = right; }
            void setRightNode(Node right) { _right = &right; }

            int getDegree();

            void traversePreOrder(std::vector<T> &traverseMemory);
            void traverseInOrder(std::vector<T> &traverseMemory);
            void traversePostOrder(std::vector<T> &traverseMemory);

            static Node *generateWithPreAndInOrder(std::vector<T> preOrder, std::vector<T> inOrder);
            static Node *generateWithPostAndInOrder(std::vector<T> postOrder, std::vector<T> inOrder);

        private:
            T _data;
            Node *_left, *_right;
        };

        BinaryTree(Node *root) : _root(root){};

        Node *_root;
    };

}

#endif