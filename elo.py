# 初期設定
K = 30

# プレイヤーリスト
players = ["A", "B", "C", "D", "E", "F", "G", "H"]

results = [
    [True,	True,	True,	False,	False,	True,	False,	False],
    [True,	True,	True,	False,	False,	True,	False,	False],
    [True,	True,	False,	False,	False,	True,	True,	False],
    [True,	True,	True,	True,	False,	False,	False,	False],
    [False,	True,	False,	True,	False,	True,	False,	True],
    [True,	True,	False,	False,	True,	True,	True,	False],
    [False,	True,	True,	True,	False,	False,	True,	False],
    [False,	True,	True,	True,	False,	False,	True,	False],
    [True,	True,	True,	False,	False,	True,	False,	False],
    [True,	True,	False,	False,	True,	False,	True,	False],
    [True,	True,	False,	False,	False,	True,	True,	False],
    [True,	True,	True,	False,	False,	True,	False,	False],
    [True,	False,	True,	True,	False,	False,	False,	True],
    [True,	False,	False,	False,	True,	True,	True,	False],
    [False,	False,	True,	True,	False,	True,	False,	True],
    [True,	True,	False,	False,	True,	True,	True,	False],
    [True,	True,	True,	False,	False,	False,	False,	False],
    [False,	True,	True,	True,	False,	False,	True,	False],
    [True,	False,	False,	False,	True,	True,	True,	False]
]
initial_elo = 2000.0
elo_ratings = {player: initial_elo for player in players}
total_matches = len(results)


def compute_elo(r1, r2, s1):
    e1 = 1 / (1 + 10**((r2 - r1) / 400))
    e2 = 1 - e1
    new_r1 = r1 + K * (s1 - e1)
    new_r2 = r2 + K * (1 - s1 - e2)
    return new_r1, new_r2


# 各プレイヤーの勝利数と敗北数を計算
wins_losses = {player: {'wins': 0, 'losses': 0} for player in players}

for match in results:
    for i, win in enumerate(match):
        if win:
            wins_losses[players[i]]['wins'] += 1
        else:
            wins_losses[players[i]]['losses'] += 1

# 各プレイヤーの勝率を計算し、それを元にレーティングを計算
for player, win_loss in wins_losses.items():
    win_rate = win_loss['wins'] / total_matches
    # レーティングの計算: 初期値は1500、勝率0.5で変動なし、勝率が高ければレーティング上昇、低ければ下降
    elo_ratings[player] = initial_elo + (2 * K * (win_rate - 0.5))

print(elo_ratings)
