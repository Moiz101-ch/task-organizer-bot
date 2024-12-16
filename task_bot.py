import os
import logging
import csv
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    filename="task_bot.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# State transition model for tasks
class TaskState:
    CREATED = "Created"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    ARCHIVED = "Archived"

class Task:
    def __init__(self, task_id, description, priority):
        self.task_id = task_id
        self.description = description
        self.priority = priority
        self.state = TaskState.CREATED

    def update_state(self, new_state):
        if new_state in [TaskState.IN_PROGRESS, TaskState.COMPLETED, TaskState.ARCHIVED]:
            self.state = new_state
        else:
            raise ValueError(f"Invalid state transition: {new_state}")
        
    def __repr__(self):
        return f"Task(ID={self.task_id}, Description='{self.description}', Priority='{self.priority}', State='{self.state}')"   

class TaskOrganizerBot:
    def __init__(self):
        self.tasks = []
        self.task_counter = 1

    def add_task(self, description, priority):
        task = Task(self.task_counter, description, priority)
        self.tasks.append(task)
        self.task_counter += 1
        logging.info(f"Task added: {task}")
        return task   

    def update_task_state(self, task_id, new_state):
        try:
            task = next(t for t in self.tasks if t.task_id == task_id)
            task.update_state(new_state)
            logging.info(f"Task updated: {task}")
        except StopIteration:
            logging.error(f"Task ID {task_id} not found.")
            raise ValueError("Task ID not found.")
        except Exception as e:
            logging.error(f"Unexpected error updating task state: {e}")
            raise

    def generate_report(self, output_file="tasks_report.csv"):
        try:
            with open(output_file, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Task ID", "Description", "Priority", "State"])
                for task in self.tasks:
                    writer.writerow([task.task_id, task.description, task.priority, task.state])
            logging.info("Report generated successfully.")
            return output_file
        except Exception as e:
            logging.error(f"Failed to generate report: {e}")
            raise

if __name__ == "__main__":
    try:
        # Initialize bot
        bot = TaskOrganizerBot()

        # Add tasks
        bot.add_task("Complete Python bot project", "High")
        bot.add_task("Prepare presentation slides", "Medium")
        bot.add_task("Submit assignment", "High")

        # Update task state
        bot.update_task_state(1, TaskState.IN_PROGRESS)
        bot.update_task_state(1, TaskState.COMPLETED)

        # Generate task report
        report_file = bot.generate_report()
        print(f"Task report generated: {report_file}")

    except Exception as main_exception:
        logging.critical(f"Unexpected error in TaskOrganizerBot: {main_exception}")