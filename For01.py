
def main(n):
    """
    Return numbers from zero to n in a list view.
    Args:
        n: int
    Returns:
        list: return  answer
    """
    answer = []
    for i in range(n):
        answer.append(i)

    return answer


print(main(4))