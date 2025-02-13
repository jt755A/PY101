# function

# input: 3 args: integer grades
    # no need to check for negative / geater than one hundred
# output: letter grade (string)

# 90 <= score <= 100: 'A'
# 80 <= score < 90: 'B'
# 70 <= score < 80: 'C'
# 60 <= score < 70: 'D'
# 0 <= score < 60: 'F'

# given 3 args
    # find average:
        # separate function (in case number of grades changed)
            # given list/tuple: sum / length of (list/tuple)
            # round down result using floor division


# increasing if/elif/else block for scores

    #  sum(arg1, arg2, arg3) / 3


def average(lst):
    return sum(lst) / len(lst)

def get_grade(score1, score2, score3):
    scores = [score1, score2, score3]
    average_score = average(scores)

    if 0 <= average_score < 60:
        return 'F'
    elif 60 <= average_score < 70:
        return 'D'
    elif 70 <= average_score < 80:
        return 'C'
    elif 80 <= average_score < 90:
        return 'B'
    elif 90 <= average_score <= 1000:
        return 'A'
    
print(get_grade(95, 90, 93) == "A")      # True
print(get_grade(50, 50, 95) == "D")      # True