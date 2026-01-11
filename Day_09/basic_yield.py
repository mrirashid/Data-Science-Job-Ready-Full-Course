## yield values VS return values

def generator():
    save_stack_fram(state, line_number)
    yield 1

    restore_stack_frame(state)
    save_stack_frame(state, line_number)
    yield 2
