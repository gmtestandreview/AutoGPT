import logging
from typing import TYPE_CHECKING, Any, cast

try:
    from dotenv import load_dotenv  # type: ignore
    load_dotenv()
except ImportError:
    pass

if TYPE_CHECKING:
    from backend.util.process import AppProcess

logger = logging.getLogger(__name__)


def run_processes(*processes: "AppProcess", **kwargs: Any) -> None:
    """
    Execute all processes in the app. The last process is run in the foreground.
    Includes enhanced error handling and process lifecycle management.
    """
    try:
        # Run all processes except the last one in the background.
        for process in processes[:-1]:
            cast(Any, process).start(background=True, silent=False)

        # Run the last process in the foreground.
        cast(Any, processes[-1]).start(background=False, silent=False)
    finally:
        for process in processes:
            try:
                process.stop()
            except Exception as e:
                logger.exception(f"[{process.service_name}] unable to stop: {e}")


def main(**kwargs: Any) -> None:
    """
    Run all the processes required for the AutoGPT-server (REST and WebSocket APIs).
    """

    from backend.api.rest_api import AgentServer
    from backend.api.ws_api import WebsocketServer
    from backend.executor import DatabaseManager, ExecutionManager, Scheduler
    from backend.notifications import NotificationManager

    run_processes(
        DatabaseManager().set_log_level("warning"),
        Scheduler(),
        NotificationManager(),
        WebsocketServer(),
        AgentServer(),
        ExecutionManager(),
        **kwargs,
    )


if __name__ == "__main__":
    main()
