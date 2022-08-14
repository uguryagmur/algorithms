#include <bits/stdc++.h>
#include "binary_tree.h"
#include "gtest.h"

#define print_cont(arr)        \
    for (auto e : arr)         \
        std::cout << e << " "; \
    std::cout << std::endl;

#define print_map(arr)                                  \
    for (auto e : arr)                                  \
        std::cout << e.first << " " << e.second << " "; \
    std::cout << std::endl;

template class algo::BinaryTree<int>;

TEST(BinaryTreeGenerationTest, GenerationWithPreAndInOrderTraversals)
{
    std::vector<int> preOrder = {4, 7, 9, 6, 3, 2, 5, 8, 1};
    std::vector<int> inOrder = {7, 6, 9, 3, 4, 5, 8, 2, 1};
    algo::BinaryTree<int> *tree = algo::BinaryTree<int>::Generator::generateWithPreAndInOrder(preOrder, inOrder);
    EXPECT_EQ(preOrder, tree->traversePreOrder());
    EXPECT_EQ(inOrder, tree->traverseInOrder());
    delete tree;
}

TEST(BinaryTreeGenerationTest, GenerationWithPostAndInOrderTraversals)
{
    std::vector<int> postOrder = {6, 3, 9, 7, 8, 5, 1, 2, 4};
    std::vector<int> inOrder = {7, 6, 9, 3, 4, 5, 8, 2, 1};
    algo::BinaryTree<int> *tree = algo::BinaryTree<int>::Generator::generateWithPostAndInOrder(postOrder, inOrder);
    EXPECT_EQ(postOrder, tree->traversePostOrder());
    EXPECT_EQ(inOrder, tree->traverseInOrder());
    delete tree;
}