def user_profile(first_name, last_name, **profile):
    user_info_des = "User Info:"
    if first_name:
        user_info_des = user_info_des + "\nfirst_name: " + first_name
    if last_name:
        user_info_des = user_info_des + "\nlast_name: " + last_name
    for k, v in profile.items():
        user_info_des = user_info_des + "\n" + k + ": " + v

    return user_info_des


def make_food(*material):
    make_dsc = "我想定做一个三明治，有以下要求： "
    for m in material:
        make_dsc = make_dsc + "\n -" + m

    return make_dsc
