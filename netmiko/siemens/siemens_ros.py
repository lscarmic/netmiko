

from __future__ import unicode_literals
from __future__ import print_function
import time
from netmiko.base_connection import BaseConnection

# This was used in initial testing. Not sure of the difference between it and BaseConnection.

# from netmiko.terminal_server import TerminalServerSSH

# class ROSBase(TerminalServerSSH):
#     """Siemens ROS support, Tested on RS1600 and RSG2100."""
#     def session_preparation(self):
#         """Prepare the session after the connection has been established."""
#         # Ruggedcom forces an 'ENTER' after SSH connections only
#         # (but it doesn't hurt to press 'ENTER' during Telnet)
#         self.write_channel(self.RETURN)
#         time.sleep(.3 * self.global_delay_factor)
#         shell_command = chr(19)  # CTRL-S to get to shell
#         self.write_channel(shell_command)
#         time.sleep(.3 * self.global_delay_factor)
#         self._test_channel_read(pattern=r'>')
#         self.set_base_prompt()
#         self.disable_paging()
#         # Clear the read buffer
#         time.sleep(.3 * self.global_delay_factor)
#         self.clear_buffer()

class ROSBase(BaseConnection):
    """Siemens ROS support, Tested on RS1600 and RSG2100."""
    def session_preparation(self):
        """Prepare the session after the connection has been established."""
        # Ruggedcom forces an 'ENTER' after SSH connections only
        # (but it doesn't hurt to press 'ENTER' during Telnet)
        self.write_channel(self.RETURN)
        time.sleep(.3 * self.global_delay_factor)
        # Need CTRL-S to get to shell
        shell_command = chr(19)
        self.write_channel(shell_command)
        time.sleep(.3 * self.global_delay_factor)
        self._test_channel_read(pattern=r'>')
        self.set_base_prompt()
        self.disable_paging()
        # Clear the read buffer
        time.sleep(.3 * self.global_delay_factor)
        self.clear_buffer()

    def disable_paging(self, *args, **kwargs):
        """Siemens ROS software does not require this."""
        return ""

    def check_enable_mode(self, *args, **kwargs):
        """Siemens ROS software does not have an enable."""
        pass

    def enable(self, *args, **kwargs):
        """Siemens ROS software does not have an enable."""
        pass

    def exit_enable_mode(self, *args, **kwargs):
        """Siemens ROS software does not have an enable."""
        return ""

    def config_mode(self):
        """Siemens ROS software does not have a config mode."""
        self._in_config_mode = True
        return ""

    def check_config_mode(self, check_string=""):
        """Checks whether in configuration mode. Returns a boolean."""
        return self._in_config_mode

    def exit_config_mode(self, exit_config=">"):
        """Siemens ROS software does not have a config mode."""
        self._in_config_mode = False
        return ""

    def cleanup(self):
        """Gracefully exit the SSH session."""
        try:
            self.exit_config_mode()
        except Exception:
            # Always try to send 'exit' regardless of whether exit_config_mode works or not.
            pass
        self._session_log_fin = True
        self.write_channel("logout" + self.RETURN)

class ROSSSH(ROSBase):
    """ROS SSH Support."""
    #     def __init__(self, **kwargs):
    #         # Possible insertion of global_delay_factor
    #         kwargs.setdefault("global_delay_factor", 2)
    #         return super(ROSSSH, self).__init__(**kwargs)
    pass

#
#
class ROSTelnet(ROSBase):
    """Placeholder for ROS Telnet Support."""
    pass
