from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QTreeWidget, QTreeWidgetItem, QLabel
)
from PySide6.QtCore import Qt
from src.data_classes import File, FileInfo


class FileExplorer(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(600, 400)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.message_label = QLabel("No available file data")
        self.message_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.message_label)

        self.tree = QTreeWidget()
        self.tree.setColumnCount(3)
        self.tree.setColumnWidth(0, 400)
        self.tree.setHeaderLabels(["Name", "Size (KB)", "Permissions"])
        self.tree.setVisible(False)
        self.layout.addWidget(self.tree)

        self.mock_fs: dict[str, FileInfo] = {}

    def update_tree(self, path: str, file_info: FileInfo):
        self.mock_fs[path] = file_info

        # Se estiver expandindo o root ("/"), limpa tudo
        if path == "/":
            self.tree.clear()
            self._populate_node(None, path, file_info)
            self.message_label.setVisible(False)
            self.tree.setVisible(True)

    def _populate_node(self, parent_item, path: str, file_info: FileInfo):
        for folder in file_info.folders:
            folder_path = f"{path.rstrip('/')}/{folder.name}"
            folder_item = QTreeWidgetItem([
                folder.name,
                f"{folder.size:.2f}",
                folder.permissions
            ])
            folder_item.setToolTip(0, self._make_tooltip(folder))
            folder_item.setChildIndicatorPolicy(QTreeWidgetItem.ShowIndicator)
            folder_item.setData(0, Qt.UserRole, folder_path)

            if parent_item:
                parent_item.addChild(folder_item)
            else:
                self.tree.addTopLevelItem(folder_item)

        for file in file_info.files:
            file_item = QTreeWidgetItem([
                file.name,
                f"{file.size:.2f}",
                file.permissions
            ])
            file_item.setToolTip(0, self._make_tooltip(file))
            if parent_item:
                parent_item.addChild(file_item)
            else:
                self.tree.addTopLevelItem(file_item)

    def open_files_from_expanded_folder(self, item: QTreeWidgetItem, folder_path: str):

        if folder_path in self.mock_fs:
            file_info = self.mock_fs[folder_path]
            self._populate_node(item, folder_path, file_info)
        else:
            print("No data found to " + folder_path)

    def _make_tooltip(self, file: File) -> str:
        return (
            f"<b>{file.name}</b><br>"
            f"Owner: {file.owner}<br>"
            f"Size: {file.size:.2f} KB<br>"
            f"Blocks: {file.block_count} (512 bits)<br>"
            f"Last access: {file.time_since_acess:.1f} s<br>"
            f"Last modified: {file.time_since_modified:.1f} s"
        )
