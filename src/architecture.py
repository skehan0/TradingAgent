from langgraph.graph import StateGraph, START, END
from typing import TypedDict
from langsmith import traceable


class State(TypedDict):
    """State object that gets passed between nodes"""
    message: str
    response: str
    processed: bool


def llm_node(state: State) -> State:
    """Process the message with LLM"""
    # TODO: Implement actual LLM processing
    response = f"Processed: {state['message']}"
    return {
        **state,
        "response": response,
        "processed": True
    }


def send_message_node(state: State) -> State:
    """Send the processed message"""
    # TODO: Implement actual message sending logic
    print(f"Sending: {state['response']}")
    return state


@traceable
def create_graph():
    """Create and return the compiled LangGraph workflow"""
    graph = StateGraph(State)
    
    # Add nodes
    graph.add_node("llm", llm_node)
    graph.add_node("send_message", send_message_node)
    
    # Define the flow
    graph.add_edge(START, "llm")
    graph.add_edge("llm", "send_message")
    graph.add_edge("send_message", END)
    
    return graph.compile()


if __name__ == "__main__":
    # Example usage
    app = create_graph()
    
    result = app.invoke({
        "message": "Hello, world!",
        "response": "",
        "processed": False
    })
    
    print("Final result:", result)