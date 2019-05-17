# Max path sum in triangle
'''
Approach 1:
    Bottom up, get largest of left and right children value to current element.
    Reduce to single number
    Edge Case: Triangle of size 1 => Single num

Apprach 2: 
    Same as approach 1, but modifies reduced_row array rather than 
    creating a new array per iteration.

Runtime: O(m n), for triangle of m rows and n columns
Space Complexity: O(n)


Approach 3:
    Same as approach 1, but reduce triangle to a single number.
    That is, input triangle is modified

Runtime: O(m n), for triangle of m rows and n columns
Space Complexity: O(1)


'''
class Solution():
    def max_sum_triangle(self, triangle):
        return self.solution_01(triangle)
        # return self.solution_02(triangle)
        # return self.solution_03(triangle)

    #####################################
    # Approach 01
    # 
    def solution_01(self, triangle):
        if not triangle:
            return 0
        elif len(triangle) == 1:
            return triangle[0][0]

        reduced_row = triangle[-1][:]
        for top_row in triangle[-2: : -1]:
            reduced_row = self.reduce_row_01(top_row, reduced_row)

        return reduced_row[0]


    # Gets max path values from bottom to top row
    # Bottom row has 1 more element than bottom row
    def reduce_row_01(self, top_row, bottom_row):
        reduced_row = []
        for j in range(len(top_row)):
            left_child = bottom_row[j]
            right_child = bottom_row[j + 1]
            max_path_val = top_row[j] + max(left_child, right_child)
            reduced_row.append(max_path_val)

        return reduced_row


    #####################################
    # Approach 02
    # 
    def solution_02(self, triangle):
        if not triangle:
            return 0
        elif len(triangle) == 1:
            return triangle[0][0]

        reduced_row = triangle[-1][:]
        for top_row in triangle[-2: : -1]:
            self.reduce_row_02(top_row, reduced_row)

        return reduced_row[0]


    def reduce_row_02(self, top_row, bottom_row):
        for j in range(len(top_row)):
            left_child = bottom_row[j]
            right_child = bottom_row[j + 1]
            max_path_val = top_row[j] + max(left_child, right_child)
            bottom_row[j] = max_path_val

        bottom_row.pop()


    #####################################
    # Approach 03
    # 
    def solution_03(self, triangle):
        if not triangle:
            return 0
        elif len(triangle) == 1:
            return triangle[0][0]

        i_top = len(triangle) - 2
        while i_top >= 0:
            self.reduce_row_03(triangle, i_top)
            triangle.pop()
            i_top -= 1

        return triangle[0][0]
    

    # Triangle guaranteed to have i + 1 index rows
    def reduce_row_03(self, triangle, i):
        top_row = triangle[i]
        bottom_row = triangle[i + 1]

        for j in range(len(top_row)):
            left_child = bottom_row[j]
            right_child = bottom_row[j + 1]
            max_path_val = top_row[j] + max(left_child, right_child)
            top_row[j] = max_path_val

        


# Test
class Test:
    count = 0
    def run(self, result):
        self.count += 1
        if result:
            print(f"Passed test {self.count}")
        else:
            print(f"Failed test {self.count}")

        
if __name__ == '__main__':
    s = Solution()
    t = Test()


    triangle = [[3],
                [7, 4],
                [2, 4, 6],
                [8, 5, 9, 3]
                ]
    t.run(s.max_sum_triangle(triangle) == 23)


    triangle = [[8],
                [-4, 4],
                [2, 2, 6],
                [1, 1, 1, 1]
                ]
    t.run(s.max_sum_triangle(triangle) == 19)


    triangle = [[10]]
    t.run(s.max_sum_triangle(triangle) == 10)