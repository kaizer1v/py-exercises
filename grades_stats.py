grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def #print_grades(grades):
    for grade in grades:
        #print grade

def grades_sum(grades):
    total = 0
    for grade in grades: 
        total += grade
    return total
    
def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
    return average

# The total score and how far it is from the average
# variance = (average - score)^2
def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance += float((average - score) ** 2)
    result = float(variance / len(scores))
    return result

def grades_std_deviation(variance):
    return float(variance ** 0.5)
    