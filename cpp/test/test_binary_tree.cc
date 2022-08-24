#include <bits/stdc++.h>
#include "../src/binary_tree.h"
#include "gtest.h"

TEST(BinaryTreeGenerationTest, GenerationWithPreAndInOrderTraversals)
{
    std::vector<int> preOrder = {4, 7, 9, 6, 3, 2, 5, 8, 1};
    std::vector<int> inOrder = {7, 6, 9, 3, 4, 5, 8, 2, 1};
    binary_tree::Node<int> *tree = binary_tree::Node<int>::generateWithPreAndInOrder(preOrder, inOrder);
    EXPECT_EQ(preOrder, tree->traversePreOrder());
    EXPECT_EQ(inOrder, tree->traverseInOrder());
    EXPECT_EQ(3, tree->getHeight());
    delete tree;
}

TEST(BinaryTreeGenerationTest, GenerationWithPostAndInOrderTraversals)
{
    std::vector<int> postOrder = {6, 3, 9, 7, 8, 5, 1, 2, 4};
    std::vector<int> inOrder = {7, 6, 9, 3, 4, 5, 8, 2, 1};
    binary_tree::Node<int> *tree = binary_tree::Node<int>::generateWithPostAndInOrder(postOrder, inOrder);
    EXPECT_EQ(postOrder, tree->traversePostOrder());
    EXPECT_EQ(inOrder, tree->traverseInOrder());
    EXPECT_EQ(3, tree->getHeight());
    delete tree;
}