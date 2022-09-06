from turtle import *
from pydub import AudioSegment
from pydub.playback import play


title("South African Flag And Anthem")
colormode(255)
speed(10)
penup()
goto(-200, 360)
pendown()

# National Anthem
color(0, 0, 0)
write("Flag", font=("Verdana",
                    15, "bold"))

penup()
goto(-200, 305)
pendown()

# Black triangle
color(0, 0, 0)
begin_fill()
right(90)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(-200, 305)
pendown()

# Yellow triangle
color(255, 184, 28)
begin_fill()
right(300)
forward(20)
right(120)
forward(240)
right(120)
forward(240)
right(120)
forward(20)
right(60)
forward(200)
left(120)
forward(205)
end_fill()

penup()
goto(-200, 325)
pendown()

# Green section
color(0, 119, 73)
begin_fill()
left(300)
forward(30)
right(90)
forward(50)
right(30)
forward(250)
left(30)
forward(200)
right(90)
forward(50)
right(90)
forward(200)
left(30)
forward(250)
left(330)
forward(50)
right(90)
forward(30)
right(60)
forward(240)
left(120)
forward(240)
end_fill()

penup()
goto(-110, 355)
pendown()

# Orange   Section
color(224, 60, 49)  # TODO change to white
begin_fill()
right(180)
forward(210)
left(30)
forward(195)
left(90)
forward(105)
left(90)
forward(378)
end_fill()

penup()
goto(-110, 55)
pendown()

# Blue Section
color(0, 20, 137)
begin_fill()
right(180)
forward(378)
left(90)
forward(105)
left(90)
forward(190)
left(30)
forward(213)
end_fill()

penup()
goto(-200, 15)
pendown()

# # National Anthem
# color(0, 0, 0)
# write("National Anthem", font=("Verdana",
#                                15, "bold"))

# penup()
# goto(-195, -5)
# pendown()
# write("First verse", font=("Verdana",
#                            15, "italic"))

# penup()
# goto(-190, -25)
# pendown()
# write("Lord bless Africa May her glory be lifted high,", font=("Verdana",
#                                                                15, "normal"))
# penup()
# goto(-190, -45)
# pendown()
# write("Hear our prayers Lord bless us,", font=("Verdana",
#                                                15, "normal"))
# penup()
# goto(-190, -65)
# pendown()
# write("your children.", font=("Verdana",
#                               15, "normal"))

# penup()
# goto(-195, -95)
# pendown()
# write("Second verse", font=("Verdana",
#                             15, "italic"))

# penup()
# goto(-190, -115)
# pendown()
# write("Lord we ask You to protect our nation,", font=("Verdana",
#                                                       15, "normal"))
# penup()
# goto(-190, -135)
# pendown()
# write("Intervene and end all conflicts,", font=("Verdana",
#                                                 15, "normal"))
# penup()
# goto(-190, -155)
# pendown()
# write("Protect us, protect our nation,", font=("Verdana",
#                                                15, "normal"))
# penup()
# goto(-190, -175)
# pendown()
# write("Protect South Africa, South Africa.", font=("Verdana",
#                                                    15, "normal"))
# penup()
# goto(-195, -205)
# pendown()
# write("Third verse", font=("Verdana",
#                            15, "italic"))

# penup()
# goto(-190, -225)
# pendown()
# write("From the blue of our skies,",
#       font=("Verdana",  15, "normal"))

# penup()
# goto(-190, -245)
# pendown()
# write("From the depths of our seas,",
#       font=("Verdana",  15, "normal"))
# penup()
# goto(-190, -265)
# pendown()
# write("Over our everlasting mountains,",
#       font=("Verdana",  15, "normal"))
# penup()
# goto(-190, -285)
# pendown()
# write("Where the echoing crags resound,",
#       font=("Verdana",  15, "normal"))

# # Fourth verse
# penup()
# goto(-195, -315)
# pendown()
# write("Fourth verse", font=("Verdana",
#                             15, "italic"))

# penup()
# goto(-190, -335)
# pendown()
# write("Sounds the call to come together,",
#       font=("Verdana",  15, "normal"))

# penup()
# goto(-190, -355)
# pendown()
# write("And united we shall stand,",
#       font=("Verdana",  15, "normal"))
# penup()
# goto(-190, -375)
# pendown()
# write("Let us live and strive for freedom,",
#       font=("Verdana",  15, "normal"))
# penup()
# goto(-190, -395)
# pendown()
# write("In South Africa our land.",
#       font=("Verdana",  15, "normal"))
# penup()
# goto(360, 360)
# pendown()

sound = AudioSegment.from_mp3(
    '/home/anold/Documents/python/Projects/Turtle/anthem.mp3')
play(sound)
done()
