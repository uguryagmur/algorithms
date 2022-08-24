#include "binary_tree.h"

namespace binary_tree
{
    template <typename T>
    int Node<T>::getDegree()
    {
        if (_right == nullptr and _left == nullptr)
            return 0;
        else if (_left == nullptr or _right == nullptr)
            return 1;
        else
            return 2;
    }

    template <typename T>
    int Node<T>::getHeight()
    {
        if (_right == nullptr and _left == nullptr)
            return 0;
        else if (_right == nullptr)
            return _left->getHeight() + 1;
        else if (_left == nullptr)
            return _right->getHeight() + 1;
        else
            return std::max(_left->getHeight(), _right->getHeight()) + 1;
    }

    template <typename T>
    Node<T> *Node<T>::Node::generateWithPreAndInOrder(std::vector<T> preOrder, std::vector<T> inOrder)
    {
        if (preOrder.size() != inOrder.size())
            throw std::runtime_error("ERROR: Binary tree generation - preOrder and inOrder have different sizes");
        if (preOrder.size() == 0)
            return nullptr;
        typename std::vector<T>::iterator rootData = std::find(inOrder.begin(), inOrder.end(), preOrder[0]);
        int distance = std::distance(inOrder.begin(), rootData);

        std::vector<T> leftPreOrder(preOrder.begin() + 1, preOrder.begin() + distance + 1);
        std::vector<T> leftInOrder(inOrder.begin(), inOrder.begin() + distance);
        std::vector<T> rightPreOrder(preOrder.begin() + distance + 1, preOrder.end());
        std::vector<T> rightInOrder(inOrder.begin() + distance + 1, inOrder.end());

        Node<T> *leftTree = generateWithPreAndInOrder(leftPreOrder, leftInOrder);
        Node<T> *rightTree = generateWithPreAndInOrder(rightPreOrder, rightInOrder);
        return new Node(*rootData, leftTree, rightTree);
    }

    template <typename T>
    Node<T> *Node<T>::Node::generateWithPostAndInOrder(std::vector<T> postOrder, std::vector<T> inOrder)
    {
        if (postOrder.size() != inOrder.size())
            throw std::runtime_error("ERROR: Binary tree generation - preOrder and inOrder have different sizes");
        if (postOrder.size() == 0)
            return nullptr;
        typename std::vector<T>::iterator rootData = std::find(inOrder.begin(), inOrder.end(), postOrder[postOrder.size() - 1]);
        int distance = std::distance(inOrder.begin(), rootData);

        std::vector<T> leftPostOrder(postOrder.begin(), postOrder.begin() + distance);
        std::vector<T> leftInOrder(inOrder.begin(), inOrder.begin() + distance);
        std::vector<T> rightPostOrder(postOrder.begin() + distance, postOrder.end() - 1);
        std::vector<T> rightInOrder(inOrder.begin() + distance + 1, inOrder.end());

        Node<T> *leftTree = generateWithPostAndInOrder(leftPostOrder, leftInOrder);
        Node<T> *rightTree = generateWithPostAndInOrder(rightPostOrder, rightInOrder);
        return new Node(*rootData, leftTree, rightTree);
    }

    template <typename T>
    std::vector<T> Node<T>::traversePreOrder()
    {
        std::vector<T> output;
        _traversePreOrder(output);
        return output;
    }

    template <typename T>
    std::vector<T> Node<T>::traverseInOrder()
    {
        std::vector<T> output;
        _traverseInOrder(output);
        return output;
    }

    template <typename T>
    std::vector<T> Node<T>::traversePostOrder()
    {
        std::vector<T> output;
        _traversePostOrder(output);
        return output;
    }

    template <typename T>
    void Node<T>::_traversePreOrder(std::vector<T> &traverseMemory)
    {
        traverseMemory.push_back(_data);
        if (_left != nullptr)
            _left->_traversePreOrder(traverseMemory);
        if (_right != nullptr)
            _right->_traversePreOrder(traverseMemory);
    }

    template <typename T>
    void Node<T>::_traverseInOrder(std::vector<T> &traverseMemory)
    {
        if (_left != nullptr)
            _left->_traverseInOrder(traverseMemory);
        traverseMemory.push_back(_data);
        if (_right != nullptr)
            _right->_traverseInOrder(traverseMemory);
    }

    template <typename T>
    void Node<T>::_traversePostOrder(std::vector<T> &traverseMemory)
    {
        if (_left != nullptr)
            _left->_traversePostOrder(traverseMemory);
        if (_right != nullptr)
            _right->_traversePostOrder(traverseMemory);
        traverseMemory.push_back(_data);
    }
}

template class binary_tree::Node<int>;