def just_right(str1):
    if(len(str1) < 5):
        return("Your string is too short")
    elif(len(str1) > 5):
        return("Your string is too long")
    else:
        return True

print(just_right("hi"))