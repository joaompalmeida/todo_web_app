import streamlit as st
import functions as fn


def add_todo():
    value = st.session_state["new_todo"]
    fn.add_todo(value)
    st.session_state["new_todo"] = ''




st.title("My Todo App")
st.subheader("My todo application")
st.write("This is a productivity task line.")

todos = fn.load_todo_data()


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        fn.complete_todo(index)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label="Enter a todo:", placeholder="Add a new todo...", on_change=add_todo, key="new_todo")

st.text("Created by João Almeida")