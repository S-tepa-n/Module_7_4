team1 = 'Мастера кода'
team2 = 'Волшебники данных'
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = score_1 + score_2
time1_2 = team1_time + team2_time
time_avg = time1_2 / tasks_total
challenge_result = 'Победа команды Волшебники данных!'

print('В команде участников %s %s!' % (team1, team1_num))
print('Итог, сегодня в командах: %s и %s' % (team1_num, team2_num))

print('Команда {} решила задач:{}'.format(team2, score_2))
print('{} решили задачи за {} с !'.format(team2, team2_time))

print(f'Команды решили {score_1} и {score_2} задач')
print(f'Результат соревнований:{challenge_result}')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {round(time_avg, 1)} секунд на задачу.')
