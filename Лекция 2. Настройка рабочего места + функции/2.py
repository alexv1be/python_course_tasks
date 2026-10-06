# Задача #2 – олимпиада

def check_winners(scores: list, student_score: int):
    # Сортируем список баллов по убыванию и берем первые 3 результата
    top_scores = sorted(scores, reverse=True)[:3]

    # Проверяем вхождение балла Стаса в тройку лучших
    if student_score in top_scores:
        print("Вы в тройке победителей!")
    else:
        print("Вы не попали в тройку победителей.")


# Блок тестирования программы
if __name__ == "__main__":
    scores_list = [20, 48, 52, 38, 36, 13, 7, 41, 34, 24, 5, 51, 9, 14, 28]

    # Стас получил 52 балла (самый высокий результат в списке)
    check_winners(scores_list, 52)

    # Стас получил 38 баллов (4-е место)
    check_winners(scores_list, 38)