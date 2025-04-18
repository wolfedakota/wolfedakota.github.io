import heapq

# Define a backlog item structure
class BacklogItem:
    def __init__(self, id, urgency, dependencies, customer_feedback):
        self.id = id
        self.urgency = urgency  # Value from 1-10 (higher = more urgent)
        self.dependencies = dependencies  # Number of dependent tasks
        self.customer_feedback = customer_feedback  # Importance score (1-10)
        self.priority_score = 0  # Final computed priority

    # Define comparison for heapq (max-heap behavior)
    def __lt__(self, other):
        return self.priority_score > other.priority_score  

# Function to calculate priority score
def calculate_priority(item):
    weight_urgency = 0.5
    weight_dependencies = 0.3
    weight_feedback = 0.2
    
    # Priority formula (higher score = higher priority)
    item.priority_score = (
        (item.urgency * weight_urgency) +
        (item.dependencies * weight_dependencies) +
        (item.customer_feedback * weight_feedback)
    )
    return item.priority_score

# Function to prioritize backlog using a Heap (Priority Queue)
def prioritize_backlog(backlog_list):
    priority_queue = []
    
    # Compute priority scores and store in priority queue
    for item in backlog_list:
        item.priority_score = calculate_priority(item)
        heapq.heappush(priority_queue, item)  
    
    # Return sorted backlog based on highest priority
    sorted_backlog = []
    while priority_queue:
        sorted_backlog.append(heapq.heappop(priority_queue))  
    
    return sorted_backlog

# Function to get user input
def get_user_input():
    backlog = []
    num_tasks = int(input("Enter the number of backlog items: "))
    
    for i in range(1, num_tasks + 1):
        print(f"\nEnter details for Task {i}:")
        urgency = int(input("  Enter urgency (1-10): "))
        dependencies = int(input("  Enter number of dependencies: "))
        customer_feedback = int(input("  Enter customer feedback score (1-10): "))
        
        backlog.append(BacklogItem(i, urgency, dependencies, customer_feedback))
    
    return backlog

# Get user input and prioritize backlog
user_backlog = get_user_input()
sorted_backlog = prioritize_backlog(user_backlog)

# Print sorted backlog
print("\nSorted Backlog (Highest Priority First):")
for item in sorted_backlog:
    print(f"Task ID: {item.id}, Priority Score: {item.priority_score:.2f}")
