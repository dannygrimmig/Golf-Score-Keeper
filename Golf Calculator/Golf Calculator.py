#GOLF CALCULATOR
#Danny Grimmig

def new_round(date):
    course = input("Enter the name of the Course: ")
    par = int(input("Enter par for " + course + ": "))
    total = int(input("Enter your total score: "))
    return course, par, total

def calc_stats(par, total):
    score_to_par = total - par
    if score_to_par > 0:
        print("You shot", score_to_par, "over par.")
    elif score_to_par < 0:
        print("You shot", (-1) * score_to_par, "under par.")
    else:
        print("You shot even par.")

def get_score_list(fname):
    #Make a dictionary,date as the key, course par and score as values
    with open("scorecard_list.txt", "r") as infile:
        updated_score_list = []
        lines = infile.readlines()
    return lines
       
       

def append_score_list(score_list, date, course, par, total):
    new_score = (date + " " + course + " " + str(par) + " " + str(total))
    score_list.append(new_score)
    return(score_list)
            
        

def round_history_display(new_score_list):
    print()
    print("Danny Grimmig")
    print("Score Card History")
    print("--------------------------")
    print()
    print("Date     | Course          | Par | Score")
    print("-----------------------------------------")
    with open("scorecard_list.txt", "w") as f:
        for score in (new_score_list):
            print(score)
            f.write(score + "\n")
            

    
    
def main():
    date = input("Date of play (mm/dd/yy): ")
    course, par, total = new_round(date)
    calc_stats(par, total)
    score_list = get_score_list("scorecard_list.txt")
    new_score_list = append_score_list(score_list, date, course, par, total)
    round_history_display(new_score_list)
main()
