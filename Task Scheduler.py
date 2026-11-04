import heapq

class TaskScheduler:
    def __init__(self):
        self.heap = []
        
    def add_task(self, name, priority):
        heapq.heappush(self.heap, (-priority, name))
        print(f"Added Task: '{name}' with Priority: {priority}")
        
    def run_next_task(self):
        if not self.heap:
            print("No tasks in the queue!")
            return None
        
        neg_priority, name = heapq.heappop(self.heap)
        priority = -neg_priority
        print(f">> Executing Task: '{name}' (Priority: {priority})")
        return name

    def peek_next_task(self):
        if not self.heap:
            return None
        neg_priority, name = self.heap[0]
        return name, -neg_priority

if __name__ == "__main__":
    scheduler = TaskScheduler()
    
    scheduler.add_task("Study aalgorithm", priority=9)
    scheduler.add_task("do exercise", priority=3)
    scheduler.add_task("do your tasks", priority=10)
    scheduler.add_task("continue the course", priority=5)
    
    print("\n--- Starting Task Execution Order (Highest Priority First) ---")
    
    while scheduler.heap:
        scheduler.run_next_task()