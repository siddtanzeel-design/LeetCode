class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        flat = []
        new_mat = []

        for row in mat:
            for num in row:
                flat.append(num)

        if r*c != len(flat):
            return mat
        else:
            for row in range(r):
                new_mat.append(flat[row*c:row*c+c])
            return new_mat