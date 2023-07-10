import libtmux


class Tmux:
    def __init__(self, index=0):
        self.server = libtmux.Server()
        self.session = self.find_or_create_session(index)

    def find_or_create_session(self, index=0):
        session_name = f"diz_{index}"
        sessions = self.server.sessions.filter(session_name=session_name)
        if not sessions:
            session = self.server.new_session(session_name=session_name)
        else:
            session = sessions[0]
        return session

    def attach(self):
        self.run_cmd(". ./venv/bin/activate")
        self.session.attach_session()

    def run_cmd(self, command):
        window = self.session.attached_window
        pane = window.attached_pane
        pane.send_keys(command, enter=True)

    def detach(self):
        self.run_cmd("tmux detach")

    def kill(self):
        self.session.kill_session()