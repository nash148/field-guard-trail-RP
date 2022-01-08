from typing import Protocol


class CloudHandlerProtocol(Protocol):
    def auth(self, access_token: str) -> None:
        ...

    def create_folder(self, path) -> None:
        ...

    def upload_file(self, path: str, dst_path: str) -> None:
        ...
