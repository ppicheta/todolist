import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state['new todo'] + '\n'
    print(todo)
    todos.append(todo)
    functions.write_todos(todo)

#
# Local URL: http://localhost:8501
#Network URL: http://192.168.2.3:8501
# python -m streamlit.cli run C:/Projects/TodoList_app/web.py

st.title('My Todo App')
st.subheader('This is my todo app')
st.write('This will encrease my productivity')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label='Enter a new todo', key='new_todo', on_change=add_todo)
