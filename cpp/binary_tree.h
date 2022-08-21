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
        ~BinaryTree() { delete _root;}

        struct Generator
        {
            static BinaryTree<T>* generateWithPreAndInOrder(std::vector<T> preOrder, std::vector<T> inOrder);
            static BinaryTree<T>* generateWithPreAndInOrder(T preOrder[], T inOrder[], int size);
            static BinaryTree<T>* generateWithPostAndInOrder(std::vector<T> postOrder, std::vector<T> inOrder);
            static BinaryTree<T>* generateWithPostAndInOrder(T postOrder[], T inOrder[], int size);
        };

        int getTreeHeight();

        virtual std::vector<T> traversePreOrder();
        virtual std::vector<T> traverseInOrder();
        virtual std::vector<T> traversePostOrder();

    protected:
        struct Node
        {
            Node(T data) : _data(data) {};
            Node(T data, Node left, Node right) : _data(data), _right(&right), _left(&left) {};
            Node(T data, Node *left, Node *right) : _data(data), _right(right), _left(left) {};
            ~Node()
            {
                if (_left != nullptr)
                    delete _left; 
                if (_right != nullptr)
                    delete _right;
            }

            virtual const T &getData() { return _data; }
            virtual void setData(T data) { _data = data; }

            virtual const Node* getLeftNode() { return _left; }
            virtual void setLeftNode(Node* left) { _left = left; }
            virtual void setLeftNode(Node left) { _left = &left; }

            virtual const Node* getRightNode() { return _right; }
            virtual void setRightNode(Node* right) { _right = right; }
            virtual void setRightNode(Node right) { _right = &right; }

            virtual int getDegree();
            virtual int getHeight();

            virtual void traversePreOrder(std::vector<T>& traverseMemory);
            virtual void traverseInOrder(std::vector<T>& traverseMemory);
            virtual void traversePostOrder(std::vector<T>& traverseMemory);

            static Node* generateWithPreAndInOrder(std::vector<T> preOrder, std::vector<T> inOrder);
            static Node* generateWithPostAndInOrder(std::vector<T> postOrder, std::vector<T> inOrder);

        protected:
            T _data;
            Node *_left, *_right;
        };

        BinaryTree(Node *root) : _root(root) {};

        Node *_root;
    };

}

#endif