"""
Parts 1-4
Create your classes and class methods here according to the practice instructions.
As you are working on Parts 1, 2, and 4, you can run the test python file
corresponding to that section to verify that you are completing the problem
correctly.
ex: python part_1_tests.py.
"""

class Student(object):
    """Students name and addresses"""

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question(object):
    """Questons and answeres"""

    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        print self.question
        answer = raw_input(" > ")
        if answer == self.correct_answer:
            return True
        else:
            return False


class Exam(object):
    
    
    def __init__(self, name):
        self.name = name
        questions = []
        
  
    def add_question(self, question):
        self.questions.append(question)

   
    #I have worked on this for hours and hours and I am going to stop now :(
    def administer(self):
       print self.questions


        

# class StudentExam(object):

#     def __init__(self, student, exam, score=None):
#         self.student = student
#         self.exam = exam
#         self.score = score

#     def take_test(self)





