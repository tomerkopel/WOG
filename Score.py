import Utils


def add_score(difficulty):
    score_file = open(Utils.SCORES_FILE_NAME, mode='r+')
    try:
        score_number = int(score_file.read())
        new_score_number = score_number + ((difficulty*3)+5)
        score_file.seek(0, 0)
        score_file.write(str(new_score_number))
    except:
        new_score_number = (difficulty * 3) + 5
        score_file.seek(0, 0)
        score_file.write(str(new_score_number))
