import turtle
import pandas
screen=turtle.Screen()
screen.title("U.S States Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# turtle.mainloop()
# def get_mouse_click_coor(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)



data=pandas.read_csv("50_states.csv")
all_states=data.state.to_list()
total =50
is_game_on=True
while is_game_on:
    answer_state=screen.textinput(f"{total} left","Whats the state name").title()
        
    
    if answer_state=="Exit":
       break
    if answer_state in all_states: 
        total-=1
        lis=data[data.state==answer_state]
        x=int(lis["x"])
        y=int(lis["y"])   
        write=turtle.Turtle()
        write.hideturtle()
        write.penup()
        write.goto(x,y)
        write.write(answer_state)
        all_states.remove(answer_state)
        if total==0:
            is_game_on=False

new=pandas.DataFrame(all_states) 
new.to_csv("States_left.csv")



screen.exitonclick()