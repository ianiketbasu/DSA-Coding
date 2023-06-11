class SnapshotArray:
    def __init__(self, length: int):
        self.array = [{0: 0} for _ in range(length)]  # Initialize array with length and set initial values to 0
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.array[index][self.snap_id] = val

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        snapshots = self.array[index]
        while snap_id >= 0 and snap_id not in snapshots:
            snap_id -= 1
        return snapshots[snap_id] if snap_id in snapshots else 0

        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)