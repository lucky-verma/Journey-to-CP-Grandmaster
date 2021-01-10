# python3


class DataBases:
    def __init__(self, row_counts):
        self.max_row_count = max(row_counts)
        self.row_counts = row_counts
        n_tables = len(row_counts)
        self.parent = list(range(n_tables))
        self.rank = [0] * n_tables

    def get_parent(self, i):
        if i != self.parent[i]:
            self.parent[i] = self.get_parent(self.parent[i])
        return self.parent[i]

    def merge_tables(self, dst, src):
        src_parent = self.get_parent(src)
        dst_parent = self.get_parent(dst)
        if src_parent == dst_parent:
            return
        if self.rank[src_parent] > self.rank[dst_parent]:
            self.parent[dst_parent] = src_parent
            self.row_counts[src_parent] += self.row_counts[dst_parent]
            self.row_counts[dst_parent] = 0
            self.max_row_count = max(self.max_row_count, self.row_counts[src_parent])
        else:
            self.parent[src_parent] = dst_parent
            self.row_counts[dst_parent] += self.row_counts[src_parent]
            self.row_counts[src_parent] = 0
            self.max_row_count = max(self.max_row_count, self.row_counts[dst_parent])
            if self.rank[src_parent] == self.rank[dst_parent]:
                self.rank[dst_parent] += 1


def main():
    n_tables, n_queries = map(int, input().split())
    counts = list(map(int, input().split()))
    assert (n_tables == len(counts))
    db = DataBases(counts)
    for i in range(n_queries):
        dst, src = map(int, input().split())
        db.merge_tables(dst - 1, src - 1)
        print(db.max_row_count)


if __name__ == "__main__":
    main()
