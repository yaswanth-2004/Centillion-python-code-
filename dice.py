import plotly.graph_objects as go
import random

def roll_dice():
    """
    Simulates a dice roll, creates an ASCII-based bar chart using Plotly,
    and displays the result.
    """
    input("Press Enter to roll the dice...")

    # Simulate a dice roll (assuming a 6-sided die)
    dice_result = random.randint(1, 6)

    # Create an ASCII-based bar chart using Plotly
    fig = go.Figure(go.Bar(
        x=list(range(1, 7)),
        y=[1 if i == dice_result else 0 for i in range(1, 7)],
        marker_color='black'
    ))

    # Set the title of the chart to display the dice roll result
    fig.update_layout(title=f"Dice Roll Result: {dice_result}")

    # Display the bar chart
    fig.show()

if __name__ == "__main__":
    print("Welcome to Dice Roller!")

    while True:
        roll_dice()

        play_again = input("Do you want to roll again? (yes/no): ").lower()
        if play_again != 'yes':
            break
