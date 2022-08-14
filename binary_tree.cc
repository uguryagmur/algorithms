#include <bits/stdc++.h>

#include "binary_tree.h"
#define print_cont(arr)        \
    for (auto e : arr)         \
        std::cout << e << " "; \
    std::cout << std::endl;

namespace algo
{

    template <typename T>
    int BinaryTree<T>::Node::getDegree()
    {
        if (_right == nullptr and _left == nullptr)
            return 0;
        else if (_right == nullptr)
            return _left->getDegree() + 1;
        else if (_left == nullptr)
            return _right->getDegree() + 1;
        else
            return std::max(_left->getDegree(), _right->getDegree()) + 1;
    }

    template <typename T>
    void BinaryTree<T>::Node::traversePreOrder(std::vector<T> &traverseMemory)
    {
        traverseMemory.push_back(_data);
        if (_left != nullptr)
            _left->traversePreOrder(traverseMemory);
        if (_right != nullptr)
            _right->traversePreOrder(traverseMemory);
    }

    template <typename T>
    void BinaryTree<T>::Node::traverseInOrder(std::vector<T> &traverseMemory)
    {
        if (_left != nullptr)
            _left->traverseInOrder(traverseMemory);
        traverseMemory.push_back(_data);
        if (_right != nullptr)
            _right->traverseInOrder(traverseMemory);
    }

    template <typename T>
    void BinaryTree<T>::Node::traversePostOrder(std::vector<T> &traverseMemory)
    {
        if (_left != nullptr)
            _left->traversePostOrder(traverseMemory);
        if (_right != nullptr)
            _right->traversePostOrder(traverseMemory);
        traverseMemory.push_back(_data);
    }

    template <typename T>
    typename BinaryTree<T>::Node *BinaryTree<T>::Node::generateWithPreAndInOrder(std::vector<T> preOrder, std::vector<T> inOrder)
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

        BinaryTree<T>::Node *leftTree = generateWithPreAndInOrder(leftPreOrder, leftInOrder);
        BinaryTree<T>::Node *rightTree = generateWithPreAndInOrder(rightPreOrder, rightInOrder);
        return new Node(*rootData, leftTree, rightTree);
    }

    template <typename T>
    typename BinaryTree<T>::Node *BinaryTree<T>::Node::generateWithPostAndInOrder(std::vector<T> postOrder, std::vector<T> inOrder)
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

        BinaryTree<T>::Node *leftTree = generateWithPostAndInOrder(leftPostOrder, leftInOrder);
        BinaryTree<T>::Node *rightTree = generateWithPostAndInOrder(rightPostOrder, rightInOrder);
        return new Node(*rootData, leftTree, rightTree);
    }

    template <typename T>
    BinaryTree<T> *BinaryTree<T>::Generator::generateWithPreAndInOrder(T preOrder[], T inOrder[], int size)
    {
        std::vector<T> preOrderVector, inOrderVector;
        for (int i = 0; i < size; i++)
        {
            preOrderVector.push_back(preOrder[i]);
            inOrderVector.push_back(inOrder[i]);
        }
        return generateWithPreAndInOrder(preOrderVector, inOrderVector);
    }

    template <typename T>
    BinaryTree<T> *BinaryTree<T>::Generator::generateWithPostAndInOrder(std::vector<T> postOrder, std::vector<T> inOrder)
    {
        return new BinaryTree<T>(Node::generateWithPostAndInOrder(postOrder, inOrder));
    }

    template <typename T>
    BinaryTree<T> *BinaryTree<T>::Generator::generateWithPostAndInOrder(T postOrder[], T inOrder[], int size)
    {
        std::vector<T> postOrderVector, inOrderVector;
        for (int i = 0; i < size; i++)
        {
            postOrderVector.push_back(postOrder[i]);
            inOrderVector.push_back(inOrder[i]);
        }
        return generateWithPostAndInOrder(postOrderVector, inOrderVector);
    }

    template <typename T>
    BinaryTree<T> *BinaryTree<T>::Generator::generateWithPreAndInOrder(std::vector<T> preOrder, std::vector<T> inOrder)
    {
        return new BinaryTree<T>(Node::generateWithPreAndInOrder(preOrder, inOrder));
    }

    template <typename T>
    std::vector<T> BinaryTree<T>::traversePreOrder()
    {
        std::vector<T> output;
        _root->traversePreOrder(output);
        return output;
    }

    template <typename T>
    std::vector<T> BinaryTree<T>::traverseInOrder()
    {
        std::vector<T> output;
        _root->traverseInOrder(output);
        return output;
    }

    template <typename T>
    std::vector<T> BinaryTree<T>::traversePostOrder()
    {
        std::vector<T> output;
        _root->traversePostOrder(output);
        return output;
    }

}

template class algo::BinaryTree<int>;
