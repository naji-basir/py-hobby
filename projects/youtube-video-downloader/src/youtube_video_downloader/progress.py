from rich.progress import (
    BarColumn,
    DownloadColumn,
    Progress,
    TextColumn,
    TimeRemainingColumn,
    TransferSpeedColumn,
)


class DownloadProgress:
    def __init__(self) -> None:
        self.progress = Progress(
            TextColumn("[bold cyan]{task.description}"),
            BarColumn(),
            "[progress.percentage]{task.percentage:>3.0f}%",
            DownloadColumn(),
            TransferSpeedColumn(),
            TimeRemainingColumn(),
        )

        self.tasks: dict[str, int] = {}

    def __enter__(self):
        self.progress.start()
        return self

    def __exit__(self, *args):
        self.progress.stop()

    def hook(self, data: dict) -> None:
        status = data.get("status")

        if status == "downloading":
            self._handle_downloading(data)

        elif status == "finished":
            self._handle_finished(data)

    def _handle_downloading(self, data: dict) -> None:
        filename = data.get("filename", "")
        total_bytes = data.get("total_bytes") or data.get("total_bytes_estimate") or 0
        downloaded_bytes = data.get("downloaded_bytes", 0)

        stream_type = self._get_stream_type(filename)

        if stream_type not in self.tasks:
            self.tasks[stream_type] = self.progress.add_task(
                stream_type,
                total=total_bytes,
            )

        task_id = self.tasks[stream_type]

        if total_bytes:
            self.progress.update(
                task_id,
                total=total_bytes,
                completed=downloaded_bytes,
            )
        else:
            self.progress.update(
                task_id,
                completed=downloaded_bytes,
            )

    def _handle_finished(self, data: dict) -> None:
        filename = data.get("filename", "")
        stream_type = self._get_stream_type(filename)

        task_id = self.tasks.get(stream_type)

        if task_id is not None:
            total = data.get("total_bytes")

            if total:
                self.progress.update(
                    task_id,
                    total=total,
                    completed=total,
                )

    @staticmethod
    def _get_stream_type(filename: str) -> str:
        filename_lower = filename.lower()

        if ".webm" in filename_lower:
            return "Audio"

        return "Video"
