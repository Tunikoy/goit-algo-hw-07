from max_value import find_max, Node as NodeMax
from min_value import find_min, Node as NodeMin
from tree_sum import sum_tree, Node as NodeSum
from comments import create_comment_structure

# Функція для створення дерева
def create_tree():
    root = NodeMax(10)
    root.left = NodeMax(5)
    root.right = NodeMax(20)
    root.left.left = NodeMax(3)
    root.left.right = NodeMax(7)
    root.right.right = NodeMax(30)
    return root

if __name__ == "__main__":
    # Завдання 1: Найбільше значення в дереві
    root = create_tree()
    print("Найбільше значення в дереві:", find_max(root))

    # Завдання 2: Найменше значення в дереві
    root_min = create_tree()
    print("Найменше значення в дереві:", find_min(root_min))

    # Завдання 3: Сума всіх значень у дереві
    root_sum = create_tree()
    print("Сума всіх значень в дереві:", sum_tree(root_sum))

    # Завдання 4: Система коментарів
    comment_root = create_comment_structure()
    comment_root.display()
