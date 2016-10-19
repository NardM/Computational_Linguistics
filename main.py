from task import taskTwo, taskThree

text = '''Though it was winter Vadim Petrovich, the agronomist of the farm, had a busy day last Tuesday.
He began his morning with the radio, he listened to the news. At half past seven he got up, washed, did his morning
exercises at an open window, dressed and had breakfast.
Vadim Petrovich likes mornings, because he can see his family, and he can have a talk with his wife and children.
At a quarter to nine Vadim Petrovich left home. It was a cold winter day. There was a lot of snow on the ground.
The sky wasn't blue, and the sun didn't shine at all. There weren't any people in the street.
Vadim Petrovich went to the farm. It is not far from his house, so he walks there. The road was white with snow and he
couldn't walk fast. When he came to the farm, some people wanted to see and talk to him. His working day began.
At 1 o'clock he went home to have dinner. He had dinner with his wife and little daughter who does not go to school.
He ate his dinner, rested a little, and went back to the farm. Vadim Petrovich had to talk to some people,
to write some letters, and to do some other work. At 5 o'clock he had an important meeting.
And only at 8 o'clock he came home.'''
tast = taskTwo.taskTwo(text)
#tast.solve_1()
#tast.solve_2()
#tast.solve_3()
#tast.solve_4()
tack = taskThree.taskThree(text)
#tack.sort_alphabetically()

#tack.sort_list()

#tack.sort_alphabetically_reversed()
#tack.words_all()

tack.compatibility_letters()
tack.appearance_of_the_letters_to_the_position()
