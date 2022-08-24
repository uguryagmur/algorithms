#include <bits/stdc++.h>

#ifndef BINARY_TREE
#define BINARY_TREE

namespace binary_tree
{
    template <typename T>
    class Node
    {
    public:
        Node(T data) : _data(data), _right(nullptr), _left(nullptr){};
        Node(T data, Node left, Node right) : _data(data), _right(&right), _left(&left){};
        Node(T data, Node *left, Node *right) : _data(data), _right(right), _left(left){};
        ~Node()
        {
            if (_left != nullptr)
            {
                delete _left;
            }
            if (_right != nullptr)
            {
                delete _right;
            }
        }

        static Node *generateWithPreAndInOrder(std::vector<T> preOrder, std::vector<T> inOrder);
        static Node *generateWithPostAndInOrder(std::vector<T> postOrder, std::vector<T> inOrder);

        virtual int getDegree();
        virtual int getHeight();

        virtual std::vector<T> traversePreOrder();
        virtual std::vector<T> traverseInOrder();
        virtual std::vector<T> traversePostOrder();

        virtual const T &getData() { return _data; }
        virtual void setData(T data) { _data = data; }

        virtual const Node *getLeftChild() { return _left; }
        virtual void setLeftChild(Node *left) { _left = left; }
        virtual void setLeftChild(Node left) { _left = &left; }

        virtual const Node *getRightChild() { return _right; }
        virtual void setRightChild(Node *right) { _right = right; }
        virtual void setRightChild(Node right) { _right = &right; }

    protected:
        T _data;
        Node *_left, *_right;

        virtual void _traversePreOrder(std::vector<T> &traverseMemory);
        virtual void _traverseInOrder(std::vector<T> &traverseMemory);
        virtual void _traversePostOrder(std::vector<T> &traverseMemory);
    };
}

#endif