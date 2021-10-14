from cleanarchitecture_fastapi.domain import model

def test_todo_can_generate_identifier():
    todo_info = model.TodoInfo(
        name="Crêpes party",
        due_date="today",
        description="Let’s make some crêpes"
    )
    my_todo = model.Todo(info=todo_info, parent_todo=None)
    assert my_todo.identifier == "crepes_party"

def test_child_todo_has_correct_identifier():
    main_todo_info = model.TodoInfo(
        name="Crêpes party",
        due_date="today",
        description="Let’s make some crêpes"
    )
    main_todo = model.Todo(info=main_todo_info, parent_todo=None)
    child_todo_info = model.TodoInfo(
        name="buy sugar",
        due_date="today",
        description="Brown sugar makes good crêpes"
    )
    child_todo = model.Todo(info=child_todo_info, parent_todo=main_todo)
    assert child_todo.identifier == "crepes_party.buy_sugar"

