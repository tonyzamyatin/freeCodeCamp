
def computegrade(x):
    error = "Bad score"
    try:
        fscore = float(score)
    except:
        print (error)
        exit(1)
    if (fscore >= 0.0) is False:
          print (error)
          exit(1)
    else:
        if (fscore <= 1.0) is False:
              print (error)
              exit(1)
        else:
            if fscore >= 0.9:
                grade = "A"
            elif fscore >= 0.8:
                grade = "B"
            elif fscore >= 0.7:
                grade = "C"
            elif fscore >= 0.6:
                grade = "D"
            elif fscore < 0.6:
                grade = "F"
    print(grade)

score = input("Enter your score: ")
computegrade(score)
