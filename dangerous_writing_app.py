import tkinter as tk

class DangerousWritingApp:
    """A simple writing application that deletes text after inactivity."""
    
    def __init__(self, root):
        """
            Initialize the application and create the user interface.

            Args:
                root (tk.Tk): The main Tkinter window for the application.
        """
        # Store a reference to the main application window.
        self.root = root

        # Set the window title and initial size.
        self.root.title("Dangerous Writing App")
        self.root.geometry("800x600")

        # Create the main text editing area.
        # Arial 14 is used for the font, and "word" enables word wrapping.
        self.text_area = tk.Text(
            self.root,
            font=("Arial", 14),
            wrap="word"
        )

        # Make the text area expand to fill the available window space.
        # padx and pady add some spacing around the text area.
        self.text_area.pack(
            expand=True,
            fill="both",
            padx=20,
            pady=20
        )

        # Call reset_timer() whenever the user presses a key.
        self.text_area.bind("<Key>", self.reset_timer)

        # Store the ID of the currently scheduled timer.
        # None means that no timer has been scheduled yet.
        self.timer = None

        # Set the amount of time the user can stop typing before their text is deleted.
        self.timeout = 5000


    def reset_timer(self, event=None):
        """
            Reset the text deletion timer after a keyboard event.
            If a timer is already active, it is cancelled before a new
            timer is started. This ensures that the text is only deleted
            after the user has stopped typing for the full timeout period.

            Args:
                event (tk.Event, optional): The keyboard event generated
                    by Tkinter. Defaults to None.
        """
        # Cancel the existing timer, if one has been scheduled.
        # Without this, each key press would create another timer.
        if self.timer is not None:
            self.root.after_cancel(self.timer)

        # Start a new countdown using the configured timeout.
        # When the timeout expires, delete_text() will be called.
        self.timer = self.root.after(self.timeout, self.delete_text)


    def delete_text(self):
        """
            Delete all text currently entered in the text area.
            The Tkinter Text widget uses indexes to identify text positions.
            "1.0" represents the beginning of the first line, while
            tk.END represents the end of the text.
        """
        # Delete everything from the beginning of the text area
        # through the end of the text.
        self.text_area.delete("1.0", tk.END)

if __name__ == "__main__":
    """Runs the code"""
    # Create the main window
    root = tk.Tk()
    # Create the application
    app = DangerousWritingApp(root)
    # Start the GUI
    root.mainloop()