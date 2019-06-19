import random
import copy


# Game about hitting targets by entering their indexes. Don't hit the character
class HitAndMiss:
    DIFF_N = int(10)
    RAND_COMPLEXITY = int(1000)
    CHARACTER = '*'

    # Checks to see if index input x in the array ind_arr is a valid target
    def check_hit(self, ind_arr, x, n):
        if 0 <= x < n:
            if 0 <= ind_arr[x] < n:
                return True
        return False

    # removes a target and replaces it with a specific character
    def remove_hit(self, ind_arr, vis_arr, x, n):
        if 0 <= x < n:
            ind_arr[x] = -1
            vis_arr[x] = self.CHARACTER

    # shuffles the contents of the arrays
    def shuffle_target(self, ind_arr, vis_arr, n):
        # random.seed()
        for i in range(random.randrange(self.RAND_COMPLEXITY)):
            x = random.randrange(n)
            y = random.randrange(n)
            ind_arr[x], ind_arr[y] = ind_arr[y], ind_arr[x]
            vis_arr[x], vis_arr[y] = vis_arr[y], vis_arr[x]

    # Returns true if index array has no numbers between 0 and n
    def check_done(self, ind_arr, n):
        for i in range(n):
            if n > ind_arr[i] >= 0:
                return False
        return True

    # Prints index array followed by game visuals array
    def print_results(self, ind_arr, vis_arr, n):
        for i in range(n):
            print("%d, " % ind_arr[i], end="")
        for i in range(n):
            print("%s, " % vis_arr[i], end="")

    # Prints visuals array
    def print_board(self, vis_arr, n):
        for i in range(n):
            print("%s, " % vis_arr[i], end="")
        print("Pick a number between 0 and %d!" % int(self.DIFF_N-1))

    # Plays base game
    def play_game(self):
        random.seed()
        ind_arr = list(range(self.DIFF_N))
        vis_arr = list(range(1, self.DIFF_N+1))  # change this later
        random.shuffle(vis_arr)
        ori_arr = copy.copy(vis_arr)
        self.print_board(vis_arr, self.DIFF_N)
        while True:
            user_guess = input()
            try:
                val = int(user_guess)
                if self.check_hit(ind_arr, val, self.DIFF_N):
                    self.remove_hit(ind_arr, vis_arr, val, self.DIFF_N)
                    self.shuffle_target(ind_arr, vis_arr, self.DIFF_N)
                    self.print_board(vis_arr, self.DIFF_N)
                else:
                    print("You missed!")
                    self.print_results(ind_arr, vis_arr, self.DIFF_N)
                    break
                if self.check_done(ind_arr, self.DIFF_N):
                    self.print_results(ind_arr, vis_arr, self.DIFF_N)
                    break
            except ValueError:
                print("That wasn't a number from 0 to %d." % self.DIFF_N-1)
                self.print_results(ind_arr, vis_arr, self.DIFF_N)
                break

