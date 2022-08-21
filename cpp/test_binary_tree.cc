#include <bits/stdc++.h>
#include "binary_tree.h"
#include "gtest.h"

TEST(BinaryTreeGenerationTest, GenerationWithPreAndInOrderTraversals)
{
    std::vector<int> preOrder = {4, 7, 9, 6, 3, 2, 5, 8, 1};
    std::vector<int> inOrder = {7, 6, 9, 3, 4, 5, 8, 2, 1};
    algo::BinaryTree<int> *tree = algo::BinaryTree<int>::Generator::generateWithPreAndInOrder(preOrder, inOrder);
    EXPECT_EQ(preOrder, tree->traversePreOrder());
    EXPECT_EQ(inOrder, tree->traverseInOrder());
    EXPECT_EQ(3, tree->getTreeHeight());
    delete tree;
}

TEST(BinaryTreeGenerationTest, GenerationWithPostAndInOrderTraversals)
{
    std::vector<int> postOrder = {6, 3, 9, 7, 8, 5, 1, 2, 4};
    std::vector<int> inOrder = {7, 6, 9, 3, 4, 5, 8, 2, 1};
    algo::BinaryTree<int> *tree = algo::BinaryTree<int>::Generator::generateWithPostAndInOrder(postOrder, inOrder);
    EXPECT_EQ(postOrder, tree->traversePostOrder());
    EXPECT_EQ(inOrder, tree->traverseInOrder());
    EXPECT_EQ(3, tree->getTreeHeight());
    delete tree;
}