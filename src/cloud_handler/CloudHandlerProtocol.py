from typing import Protocol


class CloudHandlerProtocol(Protocol):
    def create_folder(self, path) -> None:
        ...

    def upload_file(self, path: str, dst_path: str) -> None:
        ...
