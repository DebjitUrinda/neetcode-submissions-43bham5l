class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        light, heavy = 0, len(people)-1
        counter = 0
        print(people)
        while light <= heavy:
            max_weight = people[light] + people[heavy]
            if max_weight <= limit:
                counter += 1
                light += 1
                heavy -= 1
            elif max_weight > limit:
                if people[heavy] <= limit:
                    counter += 1
                heavy -= 1

        return counter