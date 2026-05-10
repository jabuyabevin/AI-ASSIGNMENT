"""
A simple vacuum cleaner agent simulation.
Environment: two rooms, A and B, each can be Dirty or Clean.
Agent percept: (location, room status).
Agent actions: Suck, Left, Right, NoOp.
"""

class VacuumEnvironment:
    """Represents the vacuum world with two rooms."""
    def __init__(self, initial_location='A', status_A='Dirty', status_B='Dirty'):
        self.location = initial_location      # agent's current room
        self.status = {'A': status_A, 'B': status_B}  # cleanliness of each room

    def get_percept(self):
        """Return current percept: (location, dirt status of that room)."""
        return (self.location, self.status[self.location])

    def execute_action(self, action):
        """Update environment based on agent's action."""
        if action == 'Suck':
            # Cleaning action: room becomes clean
            self.status[self.location] = 'Clean'
            print(f"    Action: Suck -> {self.location} is now Clean")
        elif action == 'Left':
            # Move agent to A
            if self.location == 'B':
                self.location = 'A'
                print(f"    Action: Left -> moved to {self.location}")
            else:
                print("    Action: Left -> already at A, no movement")
        elif action == 'Right':
            # Move agent to B
            if self.location == 'A':
                self.location = 'B'
                print(f"    Action: Right -> moved to {self.location}")
            else:
                print("    Action: Right -> already at B, no movement")
        elif action == 'NoOp':
            print("    Action: NoOp (do nothing)")
        else:
            print(f"    Unknown action: {action}")

    def is_all_clean(self):
        """Return True if both rooms are clean."""
        return self.status['A'] == 'Clean' and self.status['B'] == 'Clean'

    def __str__(self):
        return f"Location: {self.location}, Rooms: {self.status}"


class ReflexVacuumAgent:
    """A simple reflex agent for the vacuum world."""
    def __init__(self):
        pass

    def decide(self, percept):
        """
        Determine action based on percept = (location, dirt_status).
        Rule: if dirty -> Suck; else if at A -> Right; else if at B -> Left.
        """
        location, dirt = percept
        if dirt == 'Dirty':
            return 'Suck'
        elif location == 'A':
            return 'Right'
        elif location == 'B':
            return 'Left'
        return 'NoOp'  # fallback


def run_simulation(steps=10, initial_status_A='Dirty', initial_status_B='Dirty'):
    """
    Run the vacuum cleaning simulation for a given number of steps.
    Environment starts with given dirt statuses.
    """
    env = VacuumEnvironment(initial_location='A', status_A=initial_status_A, status_B=initial_status_B)
    agent = ReflexVacuumAgent()
    print(f"Initial state: {env}")
    
    for step in range(1, steps + 1):
        print(f"\n--- Step {step} ---")
        percept = env.get_percept()
        print(f"Percept: {percept}")
        action = agent.decide(percept)
        print(f"Agent chooses: {action}")
        env.execute_action(action)
        print(f"State after action: {env}")
        
        if env.is_all_clean():
            print("Both rooms are clean. Stopping early.")
            break

    print("\nFinal state:", env)


if __name__ == "__main__":
    # Test: both rooms initially dirty
    run_simulation(steps=10, initial_status_A='Dirty', initial_status_B='Dirty')