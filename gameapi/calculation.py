# To check last ball as spare or not
def is_spare(value):
    if value == "/":
        return True


# To check first ball as strike or not
def is_strike(value):
    if value in ["X", "x"]:
        return True


# Checking value is empty or not
def is_empty(value):
    if value == '':
        return True


# Calculation if value is empty to minimize runtime exception
def empty_value_calculation(frame):
    score = 0
    if is_empty(frame[0]) and is_empty(frame[1]):
        frame[0] = 0
        frame[1] = 0
        score += 0
    elif is_empty(frame[0]):
        frame[0] = 0
        score += int(frame[1])
    elif is_empty([frame[1]]):
        frame[1] = 0
        score += int(frame[0])
    return score


# non digit score calculation for strike bonus/second frame after strike
def non_digit_score_for_strike(frame):
    score = 0
    if frame[0] == "-" and frame[1] == "-":
        return score
    elif frame[0] == "-":
        # Changing value string to int as database save value as CharField
        score += int(frame[1])
    elif frame[1] == "-":
        score += int(frame[0])
    return score


# calculation for strike score and bonus
def add_strike_bonus(next_frame):
    score = 10

    if is_strike(next_frame[0]):
        score += 10
    elif is_spare(next_frame[1]):
        score += 10
    elif next_frame[0] == '' or next_frame[1] == '':
        score += empty_value_calculation(next_frame)
    elif next_frame[0] != '-' and next_frame[1] != '-':
        score += int(next_frame[0]) + int(next_frame[1])

    else:
        score += non_digit_score_for_strike(next_frame)
    return score


# calculation for spare score and bonus
def add_spare_bonus(next_frame):
    score = 10

    if is_strike(next_frame[0]):
        score += 10
    elif next_frame[0] == '':
        next_frame[0] = 0
        score += 0
    elif next_frame[0] != '-':
        score += int(next_frame[0])
    elif next_frame[0] == "-":
        score += 0
    return score


# Tenth frame score with bonus if total frame score is 10
def tenth_frame_score_only(frame):
    tenth_score = 0
    if frame[0] in ['X', 'x'] or frame[1] == '/':
        if frame[2] in ['X', 'x']:
            tenth_score += 20
        else:
            tenth_score += 10 + int(frame[2])
    else:
        tenth_score += int(frame[0]) + int(frame[1])
    return tenth_score


# Total score calculation and individual frame score calculation
def calculate_total_score(score_list):
    # Empty frame list
    frame_list = []
    # Total score
    total_score = 0
    # Frame index to track each frame
    frame_idx = 0
    for i in range(0, 9):
        frame_list.append([0, 0])
    frame_list.append([0, 0, 0])
    for idx, frame in enumerate(score_list):
        if frame_idx < 10:
            # Tenth frame score calculation and adding with total score
            if frame_idx == 9:
                tenth_frame_score = tenth_frame_score_only(frame)
                total_score += tenth_frame_score
                # adding frame in total frame list to track each frame score
                frame_list[frame_idx] = tenth_frame_score
                frame_idx += 1
                # strike score calculation, adding in total score and frame score
            elif is_strike(frame[0]):
                strike_score = add_strike_bonus(score_list[idx + 1])
                total_score += strike_score
                frame_list[frame_idx] = strike_score
                frame_idx += 1
                # spare score calculation, adding in total score and frame list
            elif is_spare(frame[1]):
                spare_score = add_spare_bonus(score_list[idx + 1])
                total_score += spare_score
                frame_list[frame_idx] = spare_score
                frame_idx += 1
                # Score calculation for empty value
            elif is_empty(frame[0]) or is_empty(frame[1]):
                empty_score = empty_value_calculation(frame)
                total_score += empty_score
                frame_list[frame_idx] = empty_score
                # Score calculation for other values
            else:
                normal_score = 0
                if frame[0] == '-' and frame[1] == "-":
                    normal_score += 0
                elif frame[0] == '-':
                    normal_score += int(frame[1])
                elif frame[1] == "-":
                    normal_score += int(frame[0])
                else:
                    normal_score = int(frame[0]) + int(frame[1])
                total_score += normal_score
                frame_list[frame_idx] = normal_score
                frame_idx += 1
    # Returning total score and frame list as python tuple
    return total_score, frame_list
